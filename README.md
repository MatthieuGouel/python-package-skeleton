# Skeleton

[![license](https://img.shields.io/github/license/matthieugouel/python-package-skeleton.svg)](https://github.com/matthieugouel/python-package-skeleton/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/python-package-skeleton/badge/?version=latest)](http://python-package-skeleton.readthedocs.io/en/latest/?badge=latest)

Skeleton package to begin projects faster.

## Installation

Note : The installation into a virtualenv is heavily recommended.

If you want to install the package :

```
pip install .
```

For development purposes, you can install the package in editable mode with the dev requirements.

```
pip install -e . -r requirements-dev.txt
```

## Syntax checking

You can check the syntax using flake8 (you must have flake8 package installed first) :

```
flake8 skeleton
```

You can also use tox (you must have tox package installed first) :

```
tox -e lint
```

## Test coverage

To execute the test coverage, you must install the dev requirements (see installation section).

Then, you can run the coverage with the following command :

```
coverage run --source skeleton -m py.test
```

You can also use tox (you must have tox package installed first) :

```
tox -e test
```

## Type checking

You use annotation to do static type checking with mypy (you must have mypy package installed first) :

```
mypy skeleton
```

You can also use tox (you must have tox package installed first) :

```
tox -e type
```

## Documentation

The documentation of the project can be found under the directory `./doc/_build/html`.

To rebuild the configuration, you can use the makefile (or the make.bat for Windows users) :

```
$ cd docs/
$ make clean
$ sphinx-apidoc -F -P -o . ../skeleton
$ make html
```
