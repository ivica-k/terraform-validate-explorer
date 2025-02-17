# Testing

## Requirement
- nox (https://nox.thea.codes/en/stable/)
- pyenv (https://github.com/pyenv/pyenv)
- pytest (https://docs.pytest.org/en/stable/)

## How this works:
1. Run the Makefile to:
    - Verify that `pyenv` is installed
    - Install the required dependencies
    - Install the specified Python version
    - Configure the global Python version
    - Run `nox`

```bash
make runtest
```
