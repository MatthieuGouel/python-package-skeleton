# Contributing

Thanks for contributing ! Here is some guidelines to make your life easier during the development process.

## Installation

This project uses `pipenv` as a package manager.

For development purposes, you can install the package in editable mode with the development requirements.

```
pipenv install --dev -e .
```

## Syntax checking

You can check the syntax using flake8 :

```
flake8 {{ cookiecutter.project_slug }}
```

You can also use tox :

```
tox -e lint
```

## Test coverage

You can run the coverage with the following command :

```bash
coverage run --source {{ cookiecutter.project_slug }} -m py.test
```

You can also use tox :

```
tox -e test
```

## Type checking

If you used annotations to do static type checking with mypy :

```
mypy {{ cookiecutter.project_slug }}
```

You can also use tox :

```
tox -e type
```

## Documentation

The documentation of the project can be found under the directory `./doc/_build/html`.

To rebuild the configuration, you can use the makefile (or the make.bat for Windows users) :

```
cd docs/
make clean
sphinx-apidoc -F -P -o . ../{{ cookiecutter.project_slug }}
make html
```

## Version bumping

To update the version of the project, just run the following command according to the nature of the change.

```
bumversion [ major | minor | patch ]
```
