SHELL := /bin/bash
PYTHON_VERSIONS := 3.9 3.10 3.11 3.12 3.13.2
REQUIREMENTS := test_requirements.txt
PYENV_EXISTS := $(shell command -v pyenv)

.PHONY: all install_pyenv install_requirements install_python_versions run_test

all: install_pyenv install_requirements install_python_versions run_test

install_pyenv:
ifeq ($(PYENV_EXISTS),)
	@echo "Installing pyenv..."
	@curl https://pyenv.run | bash
else
	@echo "Pyenv is already installed."
endif

install_requirements:
	@echo "Installing test_requirements..."
	@pip install -r tests/$(REQUIREMENTS)
	@echo "Requirements installed."

install_python_versions:
	@echo "Installing Python versions..."
	@for version in $(PYTHON_VERSIONS); do pyenv install $$version || true; done
	@echo "Python versions installed."

run_test:
	@echo "Running nox..."
	@nox
	@echo "Nox execution completed."