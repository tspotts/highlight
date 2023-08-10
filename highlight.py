import re

import click

# TODO: limits opts to 1 or make multiple work?
# TODO: flags for bright-mode, case insensitive regex
# TODO: better docs
# TODO: dev guide


class ValidRegexParamType(click.ParamType):
    name = "regex"

    def convert(self, value, param, ctx):
        try:
            return re.compile(fr"(?P<{param.name}>{value})")
        except re.error:
            self.fail(f"{value!r} is not a valid regex", param, ctx)


VALID_REGEX = ValidRegexParamType()


def apply_style(matchobj):
    key, value = matchobj.groupdict().popitem()
    return click.style(value, fg=f"bright_{key}")


@click.command()
@click.version_option()
@click.argument("input_file", type=click.File("rt"), default="-", )
@click.option("--black", type=VALID_REGEX)
@click.option("--blue", type=VALID_REGEX)
@click.option("--cyan", type=VALID_REGEX)
@click.option("--green", type=VALID_REGEX)
@click.option("--magenta", type=VALID_REGEX)
@click.option("--red", type=VALID_REGEX)
@click.option("--white", type=VALID_REGEX)
@click.option("--yellow", type=VALID_REGEX)
def cli(input_file, black, blue, cyan, green, magenta, red, white, yellow):
    """
    Read from input file specified or stdin.
    """
    for line in input_file:
        if black is not None:
            line = black.sub(apply_style, line)
        if blue is not None:
            line = blue.sub(apply_style, line)
        if cyan is not None:
            line = cyan.sub(apply_style, line)
        if green is not None:
            line = green.sub(apply_style, line)
        if magenta is not None:
            line = magenta.sub(apply_style, line)
        if red is not None:
            line = red.sub(apply_style, line)
        if white is not None:
            line = white.sub(apply_style, line)
        if yellow is not None:
            line = yellow.sub(apply_style, line)

        click.echo(line, nl=False)
