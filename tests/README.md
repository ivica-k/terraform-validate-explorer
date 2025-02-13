# Testing

## Requirement
- nox (https://nox.thea.codes/en/stable/)
- pyenv (https://github.com/pyenv/pyenv)
- pytest (https://docs.pytest.org/en/stable/)

## How this works: 
1. Install `nox` and `pytest`
```bash
pip install -r requirements.txt
```
2. Run all Python versions configured in the `noxfile.py` file.

```bash
# Configure all enviroment with pyenv
for version in 3.9 3.10 3.11 3.12 3.13; do pyenv install $version; done
# run all nox scenarios
pyenv global 3.9 3.10 3.11 3.12 3.13 && nox
# output
... nox output start...
nox > Ran multiple sessions:
nox > * test-3.8: skipped
nox > * test-3.9: success
nox > * test-3.10: success
nox > * test-3.11: success
nox > * test-3.12: success
nox > * test-3.13: success
nox > * test-pypy3: skipped
... nox output end...

pyenv global 3.12 # reset back to the default version
```

3. Run tests for a specific version of Python.

```bash
python3 -m nox -s test-3.9
# output
nox > Session test-3.10 was successful.
```
