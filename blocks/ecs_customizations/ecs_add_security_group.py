"""
pip install prefect -U
pip install prefect-aws
prefect block register -m prefect_aws.ecs
"""
from prefect_aws.ecs import ECSTask, AwsCredentials

ecs = ECSTask(
    aws_credentials=AwsCredentials.load("prod"),
    image="annaprefect/prefect-s3:latest",  # example image
    cpu="256",
    memory="512",
    stream_output=True,
    configure_cloudwatch_logs=True,
    cluster="prefect",
    execution_role_arn="arn:aws:iam::123456789:role/dataflowops_ecs_execution_role",
    task_role_arn="arn:aws:iam::123456789:role/dataflowops_ecs_task_role",
    vpc_id="vpc-0ff32ab58b1c8695a",
    task_customizations=[
        {
            "op": "add",
            "path": "/networkConfiguration/awsvpcConfiguration/securityGroups",
            "value": ["sg-d72e9599956a084f5"],
        },
    ],
)
ecs.save("prod", overwrite=True)
