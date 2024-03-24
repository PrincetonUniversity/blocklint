import pytest
import blocklint.main as bl
import io
import sys
from contextlib import redirect_stdout


args = {
    "blocklist": ["blacklist", "whitelist", "master", "slave"],
    "wordlist": [],
    "exactlist": [],
}
re_args = bl.generate_re(args)

def capture_stdout(func, *args, **kwargs):
    """
    Captures and returns the stdout output of a function call.
    
    :param func: The function to call.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: A tuple containing the function's result and the captured stdout output.
    """
    f = io.StringIO()
    with redirect_stdout(f):
        result = func(*args, **kwargs)
    output = f.getvalue()
    return result, output

test_name = "docstring_test"
test_file = "tests/docstring_tests/docstring_test_file.py"
expected_issues_count = 14
expected_output = 'docstring_test:4:68: use of "whitelist"\ndocstring_test:7:17: use of "master"\ndocstring_test:33:14: use of "slave"\ndocstring_test:34:31: use of "slave"\ndocstring_test:35:5: use of "slave"\ndocstring_test:36:17: use of "slave"\ndocstring_test:57:17: use of "slave"\ndocstring_test:59:45: use of "master"\ndocstring_test:59:21: use of "slave"\ndocstring_test:62:21: use of "slave"\ndocstring_test:65:93: use of "master"\ndocstring_test:65:65: use of "slave"\ndocstring_test:67:5: use of "slave"\ndocstring_test:68:12: use of "slave"\n' 
def test_docstring_processing():
    
    total_issues = 0
    with open(test_file) as handle:
        issue_count, output = capture_stdout(bl.process_file, handle, test_name, re_args, False)
        total_issues += issue_count

        assert total_issues == expected_issues_count
        assert output == expected_output
