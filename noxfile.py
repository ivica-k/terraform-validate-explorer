import nox

@nox.session(
    python=["3.8", "3.9", "3.10", "3.11", "3.12", "pypy3"]
)
def test(session):
    session.install('pytest')
    session.run("pytest", "-vv", "tests/")