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
python manage.py test --testrunner sensible_text_test_runner.SensibleTextTestRunner
```

or set the following in your settings:

```python
TEST_RUNNER = 'sensible_text_test_runner.SensibleTextTestRunner'
```
