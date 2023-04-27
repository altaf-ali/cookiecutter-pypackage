"""Copyright (c) {{ cookiecutter.full_name }}.

This source code is licensed under the {{ cookiecutter.open_source_license }} license found in the
LICENSE file in the root directory of this source tree.
"""

from typing import Any

import pytest

{%- if cookiecutter.command_line_interface|lower in ['click', 'typer'] %}

from click.testing import Result
from {{ cookiecutter.command_line_interface|lower }}.testing import CliRunner

from {{ cookiecutter.pkg_name }}.cli import app

class CLI:
    """CLI fixcture wrapper."""

    def __init__(self) -> None:
        """Constructor."""
        self.runner = CliRunner()

    def invoke(self, *args: Any, **kwargs: Any) -> Result:
        """Invoke a CLI command.

        Args:
            *args: Positional arguments to pass to the command
            **kwargs: Keyword arguments to pass to the command

        Returns:
            Result: Exit code from the command.
        """
        return self.runner.invoke(app, *args, **kwargs)


@pytest.fixture
def cli() -> CLI:
    """Return a CLI object as a fixture.

    Returns:
        CLI: A newly instantiated CLI object.
    """
    return CLI()


{%- endif %}
