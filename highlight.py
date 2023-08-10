import re

import click

# TODO: add params for each color variant with regex validated ParamType

# bright_black
# bright_blue
# bright_cyan
# bright_green
# bright_magenta
# bright_red
# bright_white
# bright_yellow


def apply_style(matchobj):
    key, value = matchobj.groupdict().popitem()
    return click.style(value, fg=key)


@click.command()
@click.version_option()
@click.argument("input_file", type=click.File("rt"), default="-", )
@click.option("--blue", )
def cli(input_file, blue):
    """
    Read from input file specified or stdin.
    """

    blue_regex = re.compile(fr"(?P<blue>\b{blue}\b)", re.IGNORECASE) if blue else None
    # red_regex = re.compile(r"(?P<red>\bof\b)", re.IGNORECASE)

    for line in input_file:
        if blue_regex is not None:
            line = blue_regex.sub(apply_style, line)
    #    line = red_regex.sub(apply_style, line)
        click.echo(line, nl=False)
