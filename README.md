Prints failues like:

```
FAIL: app.tests.TestCase.test_method
```

rather than:

```
FAIL: test_method (app.tests.TestCase)
```

so you can select it easily when you want to run that particular failure :P (at least on iterm, which only requires a double click)

### Installation

```
pip install git+https://github.com/rapilabs/sensible-text-test-runner.git
```

### Usage

```
./manage.py test --testrunner sensible_text_test_runner.SensibleTextTestRunner
```

or set the following in your settings:

```python
TEST_RUNNER = 'sensible_text_test_runner.SensibleTextTestRunner'
```

or just run:

```
./manage.py sensible_test
```

### Show Traceback Locals

Python 3.5 introduces the useful
[`--locals`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest--locals)
option to show local variables in tracebacks.  To use this option, you must use the provided
test command:

```
./manage.py sensible_test --locals
```

NOTE: Django 1.11 will provide this ability by allowing users to pass through extra options to the test runner: https://code.djangoproject.com/ticket/26981
