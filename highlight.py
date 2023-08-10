#!/usr/bin/env python3

import fileinput

import click
from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme


class Highlighter(RegexHighlighter):
    highlights = [r"(?i)(?P<and>\band\b)", r"(?i)(?P<of>\bof\b)", r"(?i)(?P<the>\bthe\b)"]


theme = Theme({"and": "blue", "of": "red", "the": "green"})
console = Console(highlight=False, theme=theme)
highlight_text = Highlighter()


@click.command()
def cli():
    for line in fileinput.input(encoding="utf-8"):
        console.print(highlight_text(line), end=None)
