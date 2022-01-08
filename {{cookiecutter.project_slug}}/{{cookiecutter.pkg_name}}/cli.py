"""Console script for {{cookiecutter.pkg_name}}."""

{% if cookiecutter.command_line_interface|lower in ['click', 'typer'] -%}
import {{ cookiecutter.command_line_interface|lower }}


{% if cookiecutter.command_line_interface|lower == 'click' -%}

@click.command()
def main():
    """Main entrypoint."""
    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")

{%- elif cookiecutter.command_line_interface|lower == 'typer' -%}
app = typer.Typer()

@app.command()
def hello(name: str):
    """Handle CLI command 'hello'."""
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    """Handle CLI command 'goodbye'."""
    if formal:
        typer.echo(f"Goodbye {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

def main():
    """Main entrypoint."""
    app()

{%- endif %}

if __name__ == "__main__":
    main()  # pragma: no cover
{%- endif %}
