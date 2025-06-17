#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pathlib import Path
import setuptools
import seqript


_name = "Seqript"
_description = "Seqript is a recursive structured command engine."


def _get_requirements():
    _requirements = []
    with open("requirements.txt", "r", encoding="utf-8") as fp:
        _requirements.extend(fp.readlines())
        _requirements = [_l for _l in _requirements if _l]
    return _requirements


def _get_long_description():
    _long_description = ""
    with open("README.md", "r", encoding="utf-8") as fp:
        _long_description = fp.read()
    for file in Path("doc").rglob("*.md"):
        if file.suffixes != [".md"]:
            continue
        with open(file, "r", encoding="utf-8") as fp:
            _long_description += "\n\n" + fp.read()
    return _long_description


setuptools.setup(
    name = _name,
    description = _description,
    long_description = _get_long_description(),
    long_description_content_type = "text/markdown",
    version=seqript.__version__,
    license = seqript.__license__,
    author = seqript.__author__,
    author_email = "dont@email.me",
    url = seqript.__url__,
    project_urls = {
        "Bug Reports": seqript.__url__ + "/issues",
        "Source": seqript.__url__,
    },
    packages = setuptools.find_namespace_packages(include=["seqript*"]),
    python_requires = ">=3.11, <4",
    install_requires=_get_requirements(),
    keywords = [
        "sequential",
        "sarallel"
        "script",
        "Tarcadia",
    ],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
)
