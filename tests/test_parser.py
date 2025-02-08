import sys
import pytest
import os
import json

from inputs_outputs import *


with open("tests/assets/to_validate.json", "r", encoding="utf-8") as file:
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
    "test_input,expected,text_to_filter",
    [
        (
            {  # this is test input
                "errors": [{"detail": "Public access is enabled"}],
                "warnings": [
                    {"address": "Instance type not specified 1"},
                    {"address": "Public access is enabled"},
                ],
            },
            (  # this is the expected result
                [{"detail": "Public access is enabled"}],
                [
                    {"address": "Instance type not specified 1"},
                    {"address": "Public access is enabled"},
                ],
            ),
            "Moon",  # this is the text to filter
        ),
    ],
)
def test_filter_does_not_contain(test_input, expected, text_to_filter):
    assert (
        parser.filter_does_not_contain(test_input, text_to_filter=text_to_filter)
        == expected
    )


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {  # this is test input
                "errors": [{"detail": "Public access is enabled"}],
                "warnings": [
                    {
                        "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
                    },
                    {
                        "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
                    },
                    {"address": "1.2.3.4"},
                ],
            },
            (  # this is the expected result
                [{"detail": "Public access is enabled"}],
                [
                    {
                        "address": "snowflake_grant_privileges_to_role.functions_future_read"
                    },
                    {
                        "address": "snowflake_grant_privileges_to_role.functions_future_read"
                    },
                    {"address": "3.4"},
                ],
            ),
        ),
    ],
)
def test_filter_only_unique(test_input, expected):
    assert parser.filter_only_unique(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected,regex_expression",
    [
        (
            {  # this is test input
                "errors": [{"detail": "Public access is enabled"}],
                "warnings": [
                    {"address": "Instance type not specified 1"},
                    {"address": "Public access is enabled"},
                ],
            },
            (  # this is the expected result
                [{"detail": "Public access is enabled"}],
                [{"address": "Public access is enabled"}],
            ),
            "Public",  # this is the text of regex
        ),
    ],
)
def test_filter_regex(test_input, expected, regex_expression):
    assert (
        parser.filter_regex(test_input, regex_expression=regex_expression) == expected
    )
