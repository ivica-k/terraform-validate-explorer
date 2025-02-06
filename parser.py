import re
from typing import List, Tuple


def validation_file_valid(data: dict):
    """
    Validates the output ot 'terraform validate' against a known schema
    :param data: Dictionary of output from 'terraform validate'
    :return:
    """
    try:
        for key in [
            "format_version",
            "valid",
            "error_count",
            "warning_count",
            "diagnostics",
        ]:
            _ = data[key]

        return True

    except KeyError:
        return False


def get_initial_data(data: dict) -> dict[str, List[str]]:
    """
    Parses errors and warnings to fill in the TreeWidget initially, without filtering
    :param data: Dictionary of output from 'terraform validate'
    :return: Tuple of lists with errors and warnings
    """
    errors = []
    warnings = []

    for elem in data.get("diagnostics"):
        if elem.get("severity").lower() == "warning":
            warnings.append(elem)
        elif elem.get("severity").lower() == "error":
            errors.append(elem)

    assert len(warnings) == data.get(
        "warning_count"
    ), f"Number of parsed warnings, {len(warnings)}, should be the same as the number of warnings in the file, which is {data.get('warning_count')}"
    assert len(errors) == data.get(
        "error_count"
    ), f"Number of parsed errors, {len(errors)}, should be the same as the number of errors in the file, which is {data.get('error_count')}"

    return {
        "errors": errors,
        "warnings": warnings,
    }


def filter_contains(data: dict, text_to_filter: str) -> Tuple[List[str], List[str]]:
    """
    Parses errors and warnings, filtering those that contain the `text_to_filter`
    :param data: Dictionary of output from 'terraform validate'
    :param text_to_filter: Text to search for in errors and warning messages
    :return: Tuple of lists with errors and warnings
    """
    warnings = [
        elem
        for elem in data.get("warnings", [])
        if text_to_filter in elem.get("address")
    ]
    errors = [
        elem for elem in data.get("errors", []) if text_to_filter in elem.get("detail")
    ]

    return errors, warnings


def filter_does_not_contain(
    data: dict, text_to_filter: str
) -> Tuple[List[str], List[str]]:
    """
    Parses errors and warnings, filtering those that does not contain the `text_to_filter`
    :param data: Dictionary of output from 'terraform validate'
    :param text_to_filter: Text to avoid in errors and warning messages
    :return: Tuple of lists with errors and warnings
    """
    warnings = [
        elem
        for elem in data.get("warnings", [])
        if text_to_filter not in elem.get("address")
    ]
    errors = [
        elem
        for elem in data.get("errors", [])
        if text_to_filter not in elem.get("detail")
    ]

    return errors, warnings


def _resource_address_from_full_address(address: str):
    """
    Returns the `resource_class.resource_name` from a full resource address. If a full resource address is
    'module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read', then `resource_class.resource_name`
    address is 'snowflake_grant_privileges_to_role.functions_future_read'
    :param address: Full resource address, such as 'module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read'
    :return:
    """
    return ".".join(address.split(".")[-2:])


def filter_only_unique(
    data: dict,
) -> Tuple[List[str], List[str]]:
    """
    Parses errors and warnings, returning only unique resource addresses. If a full resource address is
    'module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read', then a unique resource
    address is 'snowflake_grant_privileges_to_role.functions_future_read'
    :param data: Dictionary of output from 'terraform validate'
    :return: Tuple of lists with errors and warnings with unique resource addresses
    """
    warnings = data.get("warnings")
    warnings = [
        {key: _resource_address_from_full_address(value) for key, value in d.items()}
        for d in warnings
    ]

    errors = list({elem.get("detail"): elem for elem in data.get("errors")}.values())

    return errors, warnings


def filter_regex(data: dict, regex_expression: str) -> Tuple[List[str], List[str]]:
    """
    Parses errors and warnings, filtering those that match the `regex_expression` using `re.search()`
    :param data: Dictionary of output from 'terraform validate'
    :param regex_expression: A regular expression by which the text is filtered
    :return: Tuple of lists with errors and warnings
    """
    warnings = [
        elem
        for elem in data.get("warnings", [])
        if re.search(regex_expression, elem.get("address"))
    ]
    errors = [
        elem
        for elem in data.get("errors", [])
        if re.search(regex_expression, elem.get("detail"))
    ]

    return errors, warnings
