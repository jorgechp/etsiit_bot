# Copyright (c) 2020 Jorge Chamorro Padiel, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Nox test automation file."""
from typing import List

import nox

requirements: List[str] = ["-r", "requirements.txt"]
test_requirements: List[str] = [
    *requirements,
    "pytest==5.4.3",
    "pytest-cov==2.10.0",
]
format_requirements: List[str] = ["black==19.10b0", "isort==4.3.21"]
lint_requirements: List[str] = [
    *requirements,
    *format_requirements,
    "pylint==2.5.3",
    "mypy==0.782",
    "flake8==3.8.3",
    "pycodestyle==2.6.0",
]
python_target_files = ["etsiit_bot/", "tests/"]
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
    session.run("isort", "-rc", "--check-only", "--diff", *python_target_files)


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
    session.run(
        "pytest",
        env={
            "REPO_ROOT": "REPO_ROOT_dummy",
            "TELEGRAM_TOKEN": "TELEGRAM_TOKEN_dummy",
            "PROJECT_NAME": "PROJECT_NAME_dummy",
            "PORT": "123",
        },
    )
