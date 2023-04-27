"""Copyright (c) {{ cookiecutter.full_name }}.

This source code is licensed under the {{ cookiecutter.open_source_license }} license found in the
LICENSE file in the root directory of this source tree.
"""

{% if cookiecutter.command_line_interface|lower in ['click', 'typer'] -%}
import {{ cookiecutter.command_line_interface|lower }}


{% if cookiecutter.command_line_interface|lower == 'click' -%}

@click.command()
def main() -> None:
    """Main entrypoint."""
    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")

{%- elif cookiecutter.command_line_interface|lower == 'typer' -%}
app = typer.Typer()

@app.command()
def hello(name: str) -> None:
    """Say hello to someone.

    Args:
        name: Name to display in the greeting.

    Returns:
        None
    """
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    """Say goodbye.

    Args:
        name: Name to display in the greeting.
        formal: Whether to use formal or informal greeting.

    Returns:
        None
    """
    if formal:
        typer.echo(f"Goodbye {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

def main() -> None:
    """Application's main entrypoint.

    Returns:
        None
    """
    app()

{%- endif %}

if __name__ == "__main__":
    main()
{%- endif %}
