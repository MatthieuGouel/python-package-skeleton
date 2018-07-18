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

tests:
	@$(ENVRUN) py.test

generate-docs:
	@sphinx-apidoc -M -f -o docs {{ cookiecutter.project_slug }}

clean-docs:
	@$(MAKE) clean -C ./docs

docs: generate-docs
	@$(MAKE) html -C ./docs

.PHONY: install install-dev shell format lint mypy tests docs
