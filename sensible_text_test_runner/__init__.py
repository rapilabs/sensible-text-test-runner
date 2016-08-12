import unittest
from django.test.runner import DiscoverRunner


class SensibleTextTestResult(unittest.TextTestResult):
    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return '{}.{}.{}'.format(test.__class__.__module__, test.__class__.__qualname__, test._testMethodName)


class SensibleTextTestRunner(DiscoverRunner):
    def get_resultclass(self):
        return DebugSQLTextTestResult if self.debug_sql else SensibleTextTestResult
