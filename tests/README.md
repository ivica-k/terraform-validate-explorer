# Testing

## Requirement
- nox (https://nox.thea.codes/en/stable/)
- pyenv (https://github.com/pyenv/pyenv)
- pytest (https://docs.pytest.org/en/stable/)

## How this works:

Run the Makefile to:
- Verify that `pyenv` is installed
- Install the required dependencies
- Install the specified Python version
- Configure the global Python version
- Run `nox`


```bash
# In root folder
make -f Makefile
```

## Known Issues

If you use macOS and an ARM processor, you may need to run the installation command with these parameters.

```bash
PYTHON_BUILD_HOMEBREW_OPENSSL_FORMULA=openssl@1.1 arch -x86_64 pyenv install 3.12.2
```