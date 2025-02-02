"""Copyright (c) {{ cookiecutter.full_name }}.

This source code is licensed under the {{ cookiecutter.open_source_license }} license found in the
LICENSE file in the root directory of this source tree.
"""

{%- if cookiecutter.command_line_interface|lower in ['click', 'typer'] %}

from .conftest import CLI

def test_cli_help(cli: CLI) -> None:
    """Test CLI help.

    Args:
        cli: CLI fixture

    Returns:
        None
    """
    result = cli.invoke(["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_cli_hello(cli: CLI) -> None:
    """Test hello command.

    Args:
        cli: CLI fixture

    Returns:
        None
    """
    name = "sunshine"
    result = cli.invoke(["hello", name])
    assert result.exit_code == 0
    assert name in result.stdout


def test_cli_goodbye(cli: CLI) -> None:
    """Test goodbye command.

    Args:
        cli: CLI fixture

    Returns:
        None
    """
    name = "sunshine"
    result = cli.invoke(["goodbye", name])
    assert result.exit_code == 0
    assert name in result.stdout

{%- endif %}
