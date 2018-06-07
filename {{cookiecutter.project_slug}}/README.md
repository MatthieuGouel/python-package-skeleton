# {{ cookiecutter.project_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }})
[![Coverage Status](https://img.shields.io/coveralls/github/{{ cookiecutter.username }}/{ cookiecutter.project_slug }}.svg)](https://coveralls.io/github/{{ cookiecutter.username }}/{ cookiecutter.project_slug }}?branch=master)
[![license](https://img.shields.io/github/license/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}.svg)](https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](http://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest)

{{ cookiecutter.project_short_description }}

## Installation

Note : The use of a virtual environment is heavily recommended.

If you want to install the package :

```bash
pip install .
```

For development purposes, you can install the package in editable mode with the dev requirements.

```bash
pip install -e . -r requirements-dev.txt
```

## Syntax checking

You can check the syntax using flake8 :

```bash
flake8 {{ cookiecutter.project_slug }}
```

You can also use tox :

```bash
tox -e lint
```

## Test coverage

You can run the coverage with the following command :

```bash
coverage run --source {{ cookiecutter.project_slug }} -m py.test
```

You can also use tox :

```bash
tox -e test
```

## Type checking

You use annotation to do static type checking with mypy :

```bash
mypy {{ cookiecutter.project_slug }}
```

You can also use tox :

```
tox -e type
```

## Documentation

The documentation of the project can be found under the directory `./doc/_build/html`.

To rebuild the configuration, you can use the makefile (or the make.bat for Windows users) :

```bash
$ cd docs/
$ make clean
$ sphinx-apidoc -F -P -o . ../{{ cookiecutter.project_slug }}
$ make html
```

## Version bumping

When you are satisfied with your code and you want to bump a version, just run the command :

```bash
bumversion [ major | minor | patch ]
```
