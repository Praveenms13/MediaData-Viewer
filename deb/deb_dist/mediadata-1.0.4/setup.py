from setuptools import setup, find_packages
import os

#if there is no requirements.txt file, then it automatically generate it
# generate requirements.txt
# os.popen('/usr/local/bin/pipreqs mediadata').read().splitlines()
# # read requirements.txt
# with open("mediadata/requirements.txt", "r") as f:
#     required = f.read().splitlines()

required = os.popen('/usr/local/bin/pipreqs mediadata --print').read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mediadata",
    version="1.0.4",
    author="Praveen",
    author_email="mspraveenkumar77@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A wrapper tool for mediainfo tool",
    packages=find_packages(),
    install_requires=required,
    url="https://git.selfmade.ninja/mspraveenkumar77/mediadata_pkg",
    entry_points={
        "console_scripts": ["mediadata = mediadata.mediadata:main"],
    },
)
