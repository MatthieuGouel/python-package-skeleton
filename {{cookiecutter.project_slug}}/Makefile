ENVRUN = pipenv run

install:
	@pipenv install

install-dev:
	@pipenv install --dev -e .

shell:
	@pipenv shell

format:
	@$(ENVRUN) black --py36 -l 88 -S {{ cookiecutter.project_slug }} tests

lint:
	@$(ENVRUN) flake8 {{ cookiecutter.project_slug }} tests

type:
	@$(ENVRUN) mypy {{ cookiecutter.project_slug }}

test:
	@$(ENVRUN) py.test --cov={{ cookiecutter.project_slug }} --cov-fail-under=80

.PHONY: install install-dev shell format lint mypy test
