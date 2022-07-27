from setuptools import find_packages, setup

setup(
    name="libretime-shared",
    version="1.0.0",
    description="LibreTime Shared",
    url="http://github.com/libretime/libretime",
    author="LibreTime Contributors",
    license="AGPLv3",
    packages=find_packages(exclude=["*tests*", "*fixtures*"]),
    package_data={"": ["py.typed"]},
    install_requires=[
        "click~=8.0.4",
        "loguru==0.6.0",
        "pydantic>=1.7.4,<1.10",
        "pyyaml>=5.3.1,<6.1",
    ],
    extras_require={
        "dev": [
            "types-pyyaml",
        ],
    },
)
