# Skeleton

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

## Syntax

You can check the syntax using pylama (you must have pylama package installed first) :

```
pylama skeleton
```

You can also use tox (you must have tox package installed first) :

```
tox -e pylama
```

## Test coverage

To execute the test coverage, you must install the package with the dev requirements (see installation section).

Then, you can run the coverage with the following command :

```
coverage run --source skeleton -m py.test
```

You can also use tox (you must have tox package installed first) :

```
tox -e pytest
```
