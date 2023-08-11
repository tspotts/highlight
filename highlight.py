import re

import click

# TODO: ignore-case flag?
# TODO: whole-line mode?


class ValidRegexParamType(click.ParamType):
    name = "regex string to highlight"

    def convert(self, value, param, ctx):
        try:
            return re.compile(fr"(?P<{param.name}>{value})")
        except re.error:
            self.fail(f"{value!r} is not a valid regex", param, ctx)


VALID_REGEX = ValidRegexParamType()


@click.pass_context
def apply_style(ctx, matchobj):
    key, value = matchobj.groupdict().popitem()
    return click.style(value, fg=f"bright_{key}" if ctx.params["bright"] else key)


@click.command()
@click.version_option()
@click.argument("input_file", type=click.File("rt"), default="-")
@click.option("--bright/--no-bright", default=True, help=f'{click.style("Enable", fg="bright_green")}/{click.style("Disable", fg="green")} bright mode.')
@click.option("--black", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in black.", fg="bright_black"))
@click.option("--blue", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in blue.", fg="bright_blue"))
@click.option("--cyan", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in cyan.", fg="bright_cyan"))
@click.option("--green", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in green.", fg="bright_green"))
@click.option("--magenta", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in magenta.", fg="bright_magenta"))
@click.option("--red", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in red.", fg="bright_red"))
@click.option("--white", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in white.", fg="bright_white"))
@click.option("--yellow", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in yellow.", fg="bright_yellow"))
def cli(input_file, bright, black, blue, cyan, green, magenta, red, white, yellow):
    """
    Read from the specified input file or from stdin. Regex matching and highlighting text based on options specified.
    """
    for line in input_file:
        for opt in black:
            line = opt.sub(apply_style, line)
        for opt in blue:
            line = opt.sub(apply_style, line)
        for opt in cyan:
            line = opt.sub(apply_style, line)
        for opt in green:
            line = opt.sub(apply_style, line)
        for opt in magenta:
            line = opt.sub(apply_style, line)
        for opt in red:
            line = opt.sub(apply_style, line)
        for opt in white:
            line = opt.sub(apply_style, line)
        for opt in yellow:
            line = opt.sub(apply_style, line)

        click.echo(line, nl=False)


cli(max_content_width=150)
