import re
import subprocess
from typing import Any, Dict

from loguru import logger

REPLAYGAIN_EXECUTABLE = "replaygain"  # From the rgain3 python package


def analyze_replaygain(filename: str, metadata: Dict[str, Any]):
    """Extracts the Replaygain loudness normalization factor of a track.
    :param filename: The full path to the file to analyzer
    :param metadata: A metadata dictionary where the results will be put
    :return: The metadata dictionary
    """
    """ The -d flag means do a dry-run, ie. don't modify the file directly.
    """
    command = [REPLAYGAIN_EXECUTABLE, "-d", filename]
    try:
        results = subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            close_fds=True,
            universal_newlines=True,
        )
        gain_match = (
            r"Calculating Replay Gain information \.\.\.(?:\n|.)*?:([\d.-]*) dB"
        )
        replaygain = re.search(gain_match, results).group(1)
        metadata["replay_gain"] = float(replaygain)

    except OSError as e:  # replaygain was not found
        logger.warning(
            "Failed to run: %s - %s. %s"
            % (command[0], e.strerror, "Do you have python-rgain installed?")
        )
    except subprocess.CalledProcessError as e:  # replaygain returned an error code
        logger.warning("%s %s %s", e.cmd, e.output, e.returncode)
    except Exception as e:
        logger.warning(e)

    return metadata
