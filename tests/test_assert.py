import subprocess
from pathlib import Path

import pytest

from tests.helpers import run_hook_with_file


@pytest.mark.parametrize(
    "filename,expected",
    [
        (
            "assert_and",
            "Assert with 'and' found",
        ),
        (
            "assert_missing_message",
            "Assert without a message found",
        ),
        (
            "assert_success",
            None,
        ),
    ],
)
def test_assert_checks(filename: Path, expected: str | None):
    result = run_hook_with_file("assert", filename)

    expected_returncode = 0
    if expected:
        expected_returncode = 1
        try:
            assert expected in result.stderr
        except AssertionError:
            print("Expected stderr:", expected)
            print("Actual:", result.stderr)
            raise AssertionError("stderr mismatch")

    try:
        assert result.returncode == expected_returncode
    except AssertionError:
        print("Expected returncode:", expected_returncode)
        print("Actual:", result.returncode)
        print("stderr:", result.stderr)
        raise AssertionError("returncode mismatch")
