mock_test_input = {
    "errors": [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.schemas_future_read"
        },
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.schemas_future_read"
        },
        {"address": "random_string.random"},
    ],
    "warnings": [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_write"
        },
        {"address": "module.aws.module.my_infra.aws_s3_bucket.static_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.video_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.files_encrypted"},
    ],
}

mock_expected_output_contains = (
    [],
    [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
    ],
)

mock_expected_output_does_not_contain = (
    [
        {"address": "random_string.random"},
    ],
    [
        {"address": "module.aws.module.my_infra.aws_s3_bucket.static_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.video_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.files_encrypted"},
    ],
)

mock_expected_output_unique = (
    [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.schemas_future_read"
        },
        {"address": "random_string.random"},
    ],
    [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_write"
        },
        {"address": "module.aws.module.my_infra.aws_s3_bucket.static_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.video_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.files_encrypted"},
    ],
)

mock_expected_output_regex = (
    [],
    [
        {"address": "module.aws.module.my_infra.aws_s3_bucket.static_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.video_files"},
    ],
)
