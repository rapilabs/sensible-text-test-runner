import inspect
import os
import unittest

from django.test.runner import DebugSQLTextTestResult, DiscoverRunner


class SensibleTextTestResult(unittest.TextTestResult):
    def get_vi_command(self, test):
        code_object = inspect.unwrap(getattr(test, test._testMethodName)).__code__
        return 'vi +{} {}'.format(code_object.co_firstlineno, code_object.co_filename)

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            description = '{}.{}.{}'.format(test.__class__.__module__, test.__class__.__qualname__, test._testMethodName)
            if os.environ.get('SHOW_VI', False):
                description += '\n\n' + self.get_vi_command(test)
            return description


class SensibleTextTestRunner(DiscoverRunner):
    def __init__(self, tb_locals=False, **kwargs):
        self.tb_locals = tb_locals
        super().__init__(**kwargs)

    def get_resultclass(self):
        return DebugSQLTextTestResult if self.debug_sql else SensibleTextTestResult

    def run_suite(self, suite, **kwargs):
        resultclass = self.get_resultclass()
        return self.test_runner(
            verbosity=self.verbosity,
            failfast=self.failfast,
            tb_locals=self.tb_locals,
            resultclass=resultclass,
        ).run(suite)
