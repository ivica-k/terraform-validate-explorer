mock_test_input = {
    "errors": [
        {
            "detail": "This resource is deprecated and will be removed in a future major version release. Please use snowflake_grant_privileges_to_account_role instead."
        },
        {
            "detail": "This resource is deprecated and will be removed in a future major version release. Please use aws_cloudfront_origin instead."
        },
    ],
    "warnings": [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.other_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_write"
        },
        {"address": "module.aws.module.my_infra.aws_s3_bucket.static_files"},
        {"address": "module.aws.module.my_infra.aws_s3_bucket.video_files"},
    ],
}

mock_expected_output_contains = (
    [],
    [
        {
            "address": "module.snowflake.module.my_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
        {
            "address": "module.snowflake.module.other_infra.snowflake_grant_privileges_to_role.functions_future_read"
        },
    ],
)