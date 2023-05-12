update-requirements:
	pip install -U -q pip-tools
	pip-compile --generate-hashes -o requirements/base/base.txt pyproject.toml
	pip-compile --generate-hashes --extra dev -o requirements/dev/dev.txt pyproject.toml

install-dev:
	@echo 'Installing pip-tools...'
	export PIP_REQUIRE_VIRTUALENV=true; \
	pip install -U -q pip-tools
	@echo 'Installing requirements...'
	pip-sync requirements/base/base.txt requirements/dev/dev.txt

setup:
	@echo 'Setting up the environment...'
	pip config --site set site.extra-index-url https://pypi.ehps.ncsu.edu/
	make install-dev