import re

import click
from auto_click_auto import enable_click_shell_completion_option


class ValidRegexParamType(click.ParamType):
    name = "regex string to highlight"

    def convert(self, value, param, ctx):
        try:
            return param, value
        except re.error:
            self.fail(f"{value!r} is not a valid regex", param, ctx)


VALID_REGEX = ValidRegexParamType()


@click.pass_context
def apply_style(ctx, color, text):
    return click.style(text,
                       fg=f"bright_{color}" if ctx.params["bright"] else color,
                       bold=ctx.params["bold"],
                       reverse=ctx.params["reverse_mode"],
                       )


@click.command()
@enable_click_shell_completion_option(program_name="highlight")
@click.version_option()
@click.argument("input_file", type=click.File("rt"), default="-")
@click.option("--ignore-case/--no-ignore-case", default=True, help="Case insensitive regex matching. (Default=On)")
@click.option("--line-mode/--no-line-mode", default=False, help="Regex matches will highlight the entire line. (Default=Off)")
@click.option("--bold/--no-bold", default=False, help=f'{click.style("Enable", fg="bright_green", bold=True)}/{click.style("Disable", fg="bright_green", bold=False)} bold mode. (Default=Off)')
@click.option("--bright/--no-bright", default=True, help=f'{click.style("Enable", fg="bright_green")}/{click.style("Disable", fg="green")} bright mode. (Default=On)')
@click.option("--reverse-mode/--no-reverse-mode", default=True, help=f'{click.style("Enable", fg="bright_green", reverse=True)}/{click.style("Disable", fg="bright_green", reverse=False)} inverse rendering (foreground becomes background and the other way round). (Default=On)')
@click.option("--black", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in black.", fg="bright_black"))
@click.option("--blue", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in blue.", fg="bright_blue"))
@click.option("--cyan", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in cyan.", fg="bright_cyan"))
@click.option("--green", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in green.", fg="bright_green"))
@click.option("--magenta", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in magenta.", fg="bright_magenta"))
@click.option("--red", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in red.", fg="bright_red"))
@click.option("--white", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in white.", fg="bright_white"))
@click.option("--yellow", type=VALID_REGEX, multiple=True, metavar="<regex>", help=click.style("Regex to match text and highlight in yellow.", fg="bright_yellow"))
def cli(input_file, ignore_case, line_mode, bold, bright, reverse_mode, black, blue, cyan, green, magenta, red, white, yellow):
    """
    Read from the specified input file or from stdin. Regex matching and highlighting text based on options specified.
    """
    highlights_to_apply = []
    for color in [black, blue, cyan, green, magenta, red, white, yellow]:
        for param, value in color:
            highlights_to_apply.append(re.compile(
                fr"(?P<{param.name}>{value})", flags=re.IGNORECASE if ignore_case else 0))

    if not highlights_to_apply:
        raise click.ClickException("No highlighting options specified!")

    for line in input_file:
        for hl in highlights_to_apply:
            if line_mode:
                if match := hl.search(line):
                    color, _ = match.groupdict().popitem()
                    line = apply_style(color, line)
            else:
                # matchobj.groupdict() will unpack into color, text and get passed to apply_style
                line = hl.sub(lambda matchobj: apply_style(*matchobj.groupdict().popitem()), line)
        click.echo(line, nl=False)


cli(max_content_width=150)
