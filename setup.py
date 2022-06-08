#!/usr/bin/env python
import os
import pathlib
from setuptools import setup, find_packages

# prevent com.sun.star.__init__.py from raising an import error.
os.environ["ooouno_ignore_import_error"] = "True"
from com.sun.star import __version__
# VERSION = "0.4.5"
# __version__ is not part of ooo_uno_tmpl output for com.sun.star.__init__.py
# for this reason when replacing current __init__.py __version__ must be added again.
VERSION = __version__
PKG_NAME = 'types-unopy'

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
        'typing_extensions>=3.7.4.3;python_version<"3.7"',
        'types-uno-script>=0.1.0'
    ],
    description="Type annotations for LibreOffice API",
    long_description_content_type="text/x-rst",
    long_description=README
)
