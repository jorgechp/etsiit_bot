# Copyright (c) 2021 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
import setuptools

LONG_DESC = open("README.md").read()
REQUIREMENTS = open("requirements.txt").read().splitlines()

setuptools.setup(
    name="ETSIIT Bot",
    version="0.2.0",
    author="Jorge Chamorro Padial, Luis Liñán Villafranca",
    author_email="jorgechp@yandex.com, luislivilla@gmail.com",
    description=(
        "Telegram bot that make easy to access all the relevant "
        "information related with your daylife at ETSIIT (Universidad "
        "de Granada)."
    ),
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    license="MIT",
    url="https://github.com/jorgechp/etsiit_bot/",
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["etsiitbot=etsiit_bot.__main__:main"]},
    packages=["etsiit_bot"],
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    test_suite="tests",
)