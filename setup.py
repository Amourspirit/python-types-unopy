#!/usr/bin/env python
import os
import pathlib
from setuptools import setup, find_packages
from src import __version__
# from scriptforge_stubs import __version__
PKG_NAME = 'types-unopy'
VERSION = __version__

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "README.rst") as fh:
    README = fh.read()

src_path = str(HERE / 'com')

PKG = find_packages(include='com')
extra_files = package_files(src_path)
setup(
    name=PKG_NAME,
    version=VERSION,
    package_data={'': extra_files},
    python_requires='>=3.7.0',
    url="https://github.com/Amourspirit/python-types-unopy",
    packages=['com'],
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="Apache Software License",
    keywords=['libreoffice', 'openoffice', 'typings', 'uno', 'ooouno', 'pyuno'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Typing :: Typed",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        'typing_extensions>=3.7.4.3;python_version<"3.7"'
    ],
    description="Type annotations for LibreOffice API",
    long_description_content_type="text/x-rst",
    long_description=README
)
