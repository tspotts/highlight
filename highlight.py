import fileinput

import click


@click.command()
@click.version_option()
def cli():
    for line in fileinput.input(encoding="utf-8"):
        click.echo(line, nl=False)
        # click.echo(click.style(line, fg="green") if "and" in line else line, nl=False)
