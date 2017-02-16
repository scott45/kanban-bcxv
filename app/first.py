__author__ = 'Scott Businge'

import click
import sys
import time
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from tabulate import tabulate


def app_intro():
    click.secho('!' * 40, fg='yellow')
    click.secho('-' * 40, fg='white')
    init(strip=not sys.stdout.isatty())  # # strip colors if stdout is redirected
    cprint(figlet_format('kanban board', font='big'), 'white')
    click.secho('-' * 40, fg='white')
    click.secho('!' * 40, fg='yellow')


def intro_msg():
    click.secho(
        """
    """""""""""'Add, edit, delete, and keep track of your tasks'"""""""""
        """, bold=True, fg='yellow')


def intro_header():
    click.clear()
    app_intro()

    with click.progressbar(range(50000), fill_char=click.style('(', fg='white', bg='red')) as prog_bar:
        for i in prog_bar:
            pass

    click.secho('' * 75)
    click.secho('' * 75)
    intro_msg()
