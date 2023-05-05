from setuptools import find_packages, setup

setup(
    name="libretime-worker",
    version="3.0.2",
    description="LibreTime Worker",
    author="LibreTime Contributors",
    url="https://github.com/libretime/libretime",
    project_urls={
        "Bug Tracker": "https://github.com/libretime/libretime/issues",
        "Documentation": "https://libretime.org",
        "Source Code": "https://github.com/libretime/libretime",
    },
    license="MIT",
    packages=find_packages(exclude=["*tests*", "*fixtures*"]),
    python_requires=">=3.8",
    install_requires=[
        "celery==4.4.7",
        "kombu==4.6.11",
        "mutagen>=1.45.1,<1.47",
        "requests>=2.25.1,<2.31",
    ],
    extras_require={
        "dev": [
            "requests-mock>=1.10.0,<1.11",
            "types-requests>=2.25.1,<2.30",
        ],
        "sentry": [
            "sentry-sdk>=1.15.0,<1.23",
        ],
    },
    zip_safe=False,
)
