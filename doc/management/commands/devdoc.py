import os
import webbrowser
import subprocess

from django.core.management.base import BaseCommand
from django.conf import settings


MAKEFILE_COMMANDS = (  # just a subset
    'help',
    'clean',
    'html',
    'epub',
    'latex',
    'latexpdf',
    'text',
    'texinfo',
    'info',
    'xml')


class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--no_rebuild',
            action='store_true',
            dest='no_rebuild',
            default=False,
            help='Rebuild documentation before opening it')
        parser.add_argument(
            '--no_open',
            action='store_true',
            dest='no_open',
            default=False,
            help='Open documentation in default browser')
        parser.add_argument(
            '--quiet',
            action='store_false',
            dest='quiet',
            default=False,
            help='Suppress printed feedback')
        parser.add_argument(
            '--make_command',
            action="store",
            dest='make_command',
            default='html',
            help='Command for make (defaults to \'html\')',
            choices=MAKEFILE_COMMANDS)

    def handle(self, *args, **options):

        if not options['no_rebuild']:
            self.rebuild_documentation(options)

        if not options['no_open']:
            self.open_documentation()

    def rebuild_documentation(self, options):
        make_dir = os.path.join(settings.BASE_DIR, 'doc/dev')
        output = subprocess.check_output(['make', '-C', make_dir, options['make_command']])
        if not options['quiet']:
            # noinspection PyUnresolvedReferences
            self.stdout.write(output.decode('ascii'))

    @staticmethod
    def open_documentation():
        url = "file://{BASE_DIR}/doc/static/doc/dev/index.html".format(BASE_DIR=settings.BASE_DIR)
        webbrowser.open(url, new=2)  # opens in new tab if possible
