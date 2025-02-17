import sys
import pytest
import os
import json


from tests.inputs_outputs import *


with open("assets/to_validate.json", "r", encoding="utf-8") as file:
    data = json.load(file)


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


import parser  # type: ignore


def test_validation_file_valid():
    assert parser.validation_file_valid(data) == True


def test_get_initial_data():
    assert parser.get_initial_data(data) == {
        "errors": [data["diagnostics"][1]],
        "warnings": [data["diagnostics"][0]],
    }


@pytest.mark.parametrize(
    "test_input,text_to_filter,expected_output",
    [
        (
            mock_test_input,
            "functions_future_read",
            mock_expected_output_contains,
        ),
    ],
)
def test_filter_contains(test_input, text_to_filter, expected_output):
    actual_output = parser.filter_contains(test_input, text_to_filter)
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "test_input,text_to_filter,expected_output",
    [
        (
            mock_test_input,
            "snowflake", # show all non-snowflake resources
            mock_expected_output_does_not_contain,
        ),
    ],
)
def test_filter_does_not_contain(test_input, text_to_filter, expected_output):
    actual_output = parser.filter_does_not_contain(test_input, text_to_filter=text_to_filter)
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "test_input,expected_output",
    [
        (
            mock_test_input,
            mock_expected_output_unique,
        ),
    ],
)
def test_filter_only_unique(test_input, expected_output):
    actual_output = parser.filter_only_unique(test_input)
    assert actual_output == expected_output


@pytest.mark.parametrize(
    "test_input,regex,expected_output",
    [
        (
            mock_test_input,
            ".*_files$", # returns only addresses that end in '_files'
            mock_expected_output_regex,
        ),
    ],
)
def test_filter_regex(test_input, regex, expected_output):
    actual_output = parser.filter_regex(test_input, regex)
    assert actual_output == expected_output