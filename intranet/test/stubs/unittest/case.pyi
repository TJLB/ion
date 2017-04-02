# Stubs for unittest.case (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import logging
from collections import namedtuple

DIFF_OMITTED = ...  # type: Any

class SkipTest(Exception): ...
class _ShouldStop(Exception): ...
class _UnexpectedSuccess(Exception): ...

class _Outcome:
    expecting_failure = ...  # type: Any
    result = ...  # type: Any
    result_supports_subtests = ...  # type: Any
    success = ...  # type: Any
    skipped = ...  # type: Any
    expectedFailure = ...  # type: Any
    errors = ...  # type: Any
    def __init__(self, result=None): ...
    def testPartExecutor(self, test_case, isTest=False): ...

def skip(reason): ...
def skipIf(condition, reason): ...
def skipUnless(condition, reason): ...
def expectedFailure(test_item): ...

class _BaseTestCaseContext:
    test_case = ...  # type: Any
    def __init__(self, test_case): ...

class _AssertRaisesBaseContext(_BaseTestCaseContext):
    expected = ...  # type: Any
    test_case = ...  # type: Any
    expected_regex = ...  # type: Any
    obj_name = ...  # type: Any
    msg = ...  # type: Any
    def __init__(self, expected, test_case, expected_regex=None): ...
    def handle(self, name, args, kwargs): ...

class _AssertRaisesContext(_AssertRaisesBaseContext):
    def __enter__(self): ...
    exception = ...  # type: Any
    def __exit__(self, exc_type, exc_value, tb): ...

class _AssertWarnsContext(_AssertRaisesBaseContext):
    warnings_manager = ...  # type: Any
    warnings = ...  # type: Any
    def __enter__(self): ...
    warning = ...  # type: Any
    filename = ...  # type: Any
    lineno = ...  # type: Any
    def __exit__(self, exc_type, exc_value, tb): ...

_LoggingWatcher = namedtuple('_LoggingWatcher', ['records', 'output'])

class _CapturingHandler(logging.Handler):
    watcher = ...  # type: Any
    def __init__(self): ...
    def flush(self): ...
    def emit(self, record): ...

class _AssertLogsContext(_BaseTestCaseContext):
    LOGGING_FORMAT = ...  # type: Any
    logger_name = ...  # type: Any
    level = ...  # type: Any
    msg = ...  # type: Any
    def __init__(self, test_case, logger_name, level): ...
    watcher = ...  # type: Any
    old_handlers = ...  # type: Any
    old_level = ...  # type: Any
    old_propagate = ...  # type: Any
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, tb): ...

class TestCase:
    failureException = ...  # type: Any
    longMessage = ...  # type: Any
    maxDiff = ...  # type: Any
    def __init__(self, methodName=''): ...
    def addTypeEqualityFunc(self, typeobj, function): ...
    def addCleanup(self, function, *args, **kwargs): ...
    def setUp(self): ...
    def tearDown(self): ...
    @classmethod
    def setUpClass(cls): ...
    @classmethod
    def tearDownClass(cls): ...
    def countTestCases(self): ...
    def defaultTestResult(self): ...
    def shortDescription(self): ...
    def id(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def subTest(self, msg=None, **params): ...
    def run(self, result=None): ...
    def doCleanups(self): ...
    def __call__(self, *args, **kwds): ...
    def debug(self): ...
    def skipTest(self, reason): ...
    def fail(self, msg=None): ...
    def assertFalse(self, expr, msg=None): ...
    def assertTrue(self, expr, msg=None): ...
    def assertRaises(self, expected_exception, *args, **kwargs): ...
    def assertWarns(self, expected_warning, *args, **kwargs): ...
    def assertLogs(self, logger=None, level=None): ...
    def assertEqual(self, first, second, msg=None): ...
    def assertNotEqual(self, first, second, msg=None): ...
    def assertAlmostEqual(self, first, second, places=None, msg=None, delta=None): ...
    def assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None): ...
    def assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None): ...
    def assertListEqual(self, list1, list2, msg=None): ...
    def assertTupleEqual(self, tuple1, tuple2, msg=None): ...
    def assertSetEqual(self, set1, set2, msg=None): ...
    def assertIn(self, member, container, msg=None): ...
    def assertNotIn(self, member, container, msg=None): ...
    def assertIs(self, expr1, expr2, msg=None): ...
    def assertIsNot(self, expr1, expr2, msg=None): ...
    def assertDictEqual(self, d1, d2, msg=None): ...
    def assertDictContainsSubset(self, subset, dictionary, msg=None): ...
    def assertCountEqual(self, first, second, msg=None): ...
    def assertMultiLineEqual(self, first, second, msg=None): ...
    def assertLess(self, a, b, msg=None): ...
    def assertLessEqual(self, a, b, msg=None): ...
    def assertGreater(self, a, b, msg=None): ...
    def assertGreaterEqual(self, a, b, msg=None): ...
    def assertIsNone(self, obj, msg=None): ...
    def assertIsNotNone(self, obj, msg=None): ...
    def assertIsInstance(self, obj, cls, msg=None): ...
    def assertNotIsInstance(self, obj, cls, msg=None): ...
    def assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs): ...
    def assertWarnsRegex(self, expected_warning, expected_regex, *args, **kwargs): ...
    def assertRegex(self, text, expected_regex, msg=None): ...
    def assertNotRegex(self, text, unexpected_regex, msg=None): ...
    failUnlessEqual = ...  # type: Any
    assertEquals = ...  # type: Any
    failIfEqual = ...  # type: Any
    assertNotEquals = ...  # type: Any
    failUnlessAlmostEqual = ...  # type: Any
    assertAlmostEquals = ...  # type: Any
    failIfAlmostEqual = ...  # type: Any
    assertNotAlmostEquals = ...  # type: Any
    failUnless = ...  # type: Any
    assert_ = ...  # type: Any
    failUnlessRaises = ...  # type: Any
    failIf = ...  # type: Any
    assertRaisesRegexp = ...  # type: Any
    assertRegexpMatches = ...  # type: Any
    assertNotRegexpMatches = ...  # type: Any

class FunctionTestCase(TestCase):
    def __init__(self, testFunc, setUp=None, tearDown=None, description=None): ...
    def setUp(self): ...
    def tearDown(self): ...
    def runTest(self): ...
    def id(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def shortDescription(self): ...

class _SubTest(TestCase):
    test_case = ...  # type: Any
    params = ...  # type: Any
    failureException = ...  # type: Any
    def __init__(self, test_case, message, params): ...
    def runTest(self): ...
    def id(self): ...
    def shortDescription(self): ...