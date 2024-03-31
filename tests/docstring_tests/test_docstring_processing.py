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


@pytest.mark.parametrize(
    "test_file, test_name, expected_issues_count, expected_output",
    [
        (
            "tests/docstring_tests/sample_files/docstring_test_file_1.py",
            "docstring_test_1",
            14,
            'docstring_test_1:4:68: use of "whitelist"\ndocstring_test_1:7:17: use of "master"\ndocstring_test_1:33:14: use of "slave"\ndocstring_test_1:34:31: use of "slave"\ndocstring_test_1:35:5: use of "slave"\ndocstring_test_1:36:17: use of "slave"\ndocstring_test_1:57:17: use of "slave"\ndocstring_test_1:59:45: use of "master"\ndocstring_test_1:59:21: use of "slave"\ndocstring_test_1:62:21: use of "slave"\ndocstring_test_1:65:93: use of "master"\ndocstring_test_1:65:65: use of "slave"\ndocstring_test_1:67:5: use of "slave"\ndocstring_test_1:68:12: use of "slave"\n',
        ),
        (
            "tests/docstring_tests/sample_files/docstring_test_file_2.py",
            "docstring_test_2",
            5,
            'docstring_test_2:3:29: use of "whitelist"\ndocstring_test_2:5:30: use of "master"\ndocstring_test_2:8:16: use of "slave"\ndocstring_test_2:14:29: use of "blacklist"\ndocstring_test_2:37:1: use of "whitelist"\n',
        ),
    ]

)
def test_docstring_processing(test_file, test_name, expected_issues_count, expected_output):
    
    total_issues = 0
    with open(test_file) as handle:
        issue_count, output = capture_stdout(bl.process_file, handle, test_name, re_args, False)
        total_issues += issue_count

        assert total_issues == expected_issues_count
        assert output == expected_output
