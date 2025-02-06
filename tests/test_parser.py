import sys
import os
import json

with open("tests/assets/to_validate.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with open("tests/assets/warnings_errors.json", "r", encoding="utf-8") as file:
    warnings_errors = json.load(file)

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

def test_filter_contains():
    assert parser.filter_contains(data, "moon") == ([], [])

def test_filter_does_not_contain():
    assert parser.filter_does_not_contain(data, "moon") == ([], [])

def test_filter_only_unique():
    assert parser.filter_only_unique(warnings_errors) == (
        [
            warnings_errors["errors"][2],
            warnings_errors["errors"][1],
        ],
        [
            warnings_errors["warnings"][2],
            warnings_errors["warnings"][1],
        ],
    )

def test_filter_regex():
    assert parser.filter_regex(warnings_errors, "aws_instance.") == (
        [
            warnings_errors["errors"][0],
            warnings_errors["errors"][2],
        ],
        [
            warnings_errors["warnings"][0],
            warnings_errors["warnings"][2],
        ],
    )
