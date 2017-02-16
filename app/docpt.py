__author__ = 'Scott Businge'

# !/usr/bin/env python
"""
KanBan; to do, doing and done.
Usage:
    my_KanBan todo <task_name>
    my_KanBan doing <task_id>
    my_KanBan edit <task_id>
    my_KanBan delete <task_id>
    my_KanBan list_to_do
    my_KanBan list_doing
    my_KanBan list_done
    my_KanBan list_all


    my_KanBan (-i | --interactive)
    my_KanBan (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import cmd
import click
from docopt import docopt, DocoptExit
from kanban import ToDo
import first

first.app_intro()
first.intro_header()
cd = ToDo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = 'Welcome to KanBan program!' + ' (type help for a list of commands.)'
    # prompt = click.secho("KanBan App>>", fg='blue', bg='white', bold=True)
    prompt = '(Kanban) '
    file = None

    @docopt_cmd
    def do_to_do(self, arg):
        """Usage: todo <task_name> """
        try:
            task_detail = input("Enter details :")
            cd.to_do(arg['<task_name>'], task_detail)
        except mydatabase.IntegrityError:
            return -1

    @docopt_cmd
    def do_doing(self, arg):
        """Usage: doing <task_id>"""
        try:
            task_id = int(arg['<task_id>'])
            print(cd.doing(task_id))
        except ValueError:
            print("Id should be an integer")

    @docopt_cmd
    def do_done(self, arg):
        """Usage: done <task_id>"""

        try:
            task_id = int(arg['<task_id>'])
            cd.done(task_id)
        except ValueError:
            print("Please enter an integer")

    @docopt_cmd
    def do_time_taken(self, arg):
        """Usage: time_taken <time_taken>"""

        cd.time_taken(arg['<time_taken>'])

    @docopt_cmd
    def do_list_to_do(self, arg):
        """Usage: list_to_do """

        cd.list_todo()

    @docopt_cmd
    def do_list_doing(self, arg):
        """Usage: list_doing """

        cd.list_doing()

    @docopt_cmd
    def do_list_done(self, arg):
        """Usage: list_done """

        cd.list_done()

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_all """

        cd.list_all()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thank you for using Kanban, Later')
        exit()


MyInteractive().cmdloop()
