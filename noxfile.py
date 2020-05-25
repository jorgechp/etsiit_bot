"""Nox test automation file."""
import nox
from typing import List


test_requirements: List[str] = ["pytest", "pytest-cov"]
format_requirements: List[str] = ["black", "isort"]
lint_requirements: List[str] = [
    *format_requirements,
    "pylint",
    "mypy",
    "flake8",
    "pycodestyle",
]
python_target_files = ["etsiit_bot", "tests"]
python = ["3.6", "3.7", "3.8"]

nox.options.reuse_existing_virtualenvs = True
nox.options.stop_on_first_error = False


###############################################################################
# Linting
###############################################################################
@nox.session()
def lint_python(session):
    """Lint Python source code."""
    session.log("# Linting Python files...")
    session.install(*lint_requirements)
    session.run("pylint", *python_target_files)
    session.run("mypy", *python_target_files)
    session.run("flake8", *python_target_files)
    session.run("pycodestyle", *python_target_files)
    session.run("black", "-l", "79", "--check", "--diff", *python_target_files)
    session.run("isort", "--check-only", "--diff", *python_target_files)


@nox.session()
def lint_markdown(session):
    """Lint Markdown files."""
    session.log("# Linting Markdown files...")
    session.run("mdl", "--style", ".mdl.rb", ".", external=True)


###############################################################################
# Formating
###############################################################################
@nox.session(name="format")
def python_format(session):
    """Format Python source code."""
    session.log("# Formating Python files...")
    session.install(*format_requirements)
    session.run("black", "-l", "79", *python_target_files)
    session.run("isort", *python_target_files)


###############################################################################
# Testing
###############################################################################
@nox.session(python=python)
def tests(session):
    """Run python tests."""
    session.log("# Running tests...")
    session.install(*test_requirements)
    session.run("pytest")
