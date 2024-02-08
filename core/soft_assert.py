import inspect
import types

from core import Logger


class SoftAssert:

    def __init__(self, driver):
        self.driver = driver
        self.failed_conditions = []

    def assert_(self, assert_condition, message):
        if isinstance(assert_condition, types.FunctionType):
            try:
                assert_condition()
            except AssertionError as error:
                self.add_exception(message if message else error)
        else:
            try:
                assert assert_condition
                Logger.passed(message)
            except AssertionError:
                Logger.error(self.driver, message)
                self.add_exception(message if message else 'Failed by assertion!')

    def verify_expectations(self, driver):
        Logger.attach_screenshot(driver)
        if self.failed_conditions:
            Logger.error(driver, "TEST CASE - FAILED")
            self.report_exceptions()
        else:
            Logger.info("TEST CASE - PASSED")

    def add_exception(self, message=None):
        (file_path, line, function_name) = inspect.stack()[2][1:4]
        self.failed_conditions.append(
            'Exception: {}\nFail in "{}:{}" {}()\n'.format(message, file_path, line, function_name))

    def report_exceptions(self):
        if self.failed_conditions:
            report = ['Failed conditions count: [ {} ]\n'.format(len(self.failed_conditions))]
            for index, failure in enumerate(self.failed_conditions, start=1):
                if len(self.failed_conditions) > 1:
                    report.append('{}. {}'.format(index, failure))
                else:
                    report.append(failure)
            self.failed_conditions = []
            raise AssertionError('\n'.join(report))
