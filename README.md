# Skeleton

## Installation

If you want to install the package :

```
$ pip install .
```

You can also directly install the package with the dev requirements :

```
$ pip install . -r requirements-dev.txt
```

Note : You may want to install it in a virtual environment.

## Syntax

You can check the syntax using pylint (you must have pylint package installed first) :

```
pylint --rcfile=setup.cfg skeleton
```

Or with tox (you must have tox package installed first) :

```
tox -e pylint
```

## Coverage

To see the test coverage, you must install the package with the dev requirements (see installation section).

Then, you can run the coverage with the following command :

```
$ coverage run --source skeleton -m py.test
```

Or with tox (you must have tox package installed first) :

```
tox -e pytest
```
