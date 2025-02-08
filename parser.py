import re
from typing import List, Tuple

ISSUES_URL = "https://github.com/ivica-k/terraform-validate-explorer/issues/new"


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

    if len(warnings) != data.get("warning_count"):
        raise ValueError(
            f"'warning_count' in the file is {data.get('warning_count')}, but the number of parsed warnings is "
            f"{len(warnings)}.<br /><br />This may be due to manual changes to the JSON file.<br /><br />"
            f"If you believe this is a bug, please report it via the <a href='{ISSUES_URL}'>issues page</a>."
        )

    if len(errors) != data.get("error_count"):
        raise ValueError(
            f"'error_count' in the file is {data.get('error_count')}, but the number of parsed errors is "
            f"{len(errors)}.<br /><br />This may be due to manual changes to the JSON file.<br /><br />"
            f"If you believe this is a bug, please report it via the <a href='{ISSUES_URL}'>issues page</a>."
        )

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
        elem for elem in data.get("errors", []) if text_to_filter in elem.get("address")
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
        if text_to_filter not in elem.get("address")
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
    warnings = list(
        {
            _resource_address_from_full_address(elem.get("address")): elem
            for elem in data.get("warnings")
        }.values()
    )
    errors = list({elem.get("address"): elem for elem in data.get("errors")}.values())

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
        if re.search(regex_expression, elem.get("address"))
    ]

    return errors, warnings
