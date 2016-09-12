from django.core.management.commands import test


class Command(test.Command):
    def __init__(self):
        super().__init__()
        # this seems to be more or less a temp field for storing the overridable
        # option, and is not even used in handle()
        self.test_runner = 'sensible_text_test_runner.SensibleTextTestRunner'

    def add_arguments(self, parser):
        parser.add_argument(
            '--locals', action='store_true', dest='tb_locals',
            help='Show local variables in tracebacks.'
        )
        super().add_arguments(parser)

    def handle(self, *test_labels, **options):
        if 'testrunner' not in options or not options['testrunner']:
            options['testrunner'] = 'sensible_text_test_runner.SensibleTextTestRunner'
        super().handle(*test_labels, **options)
