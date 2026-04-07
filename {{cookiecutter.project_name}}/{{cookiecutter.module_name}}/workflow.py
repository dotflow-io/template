{% if cookiecutter.checkpoint == "yes" -%}
from uuid import uuid4
{% endif -%}
from dotflow import Config, DotFlow
{% if cookiecutter.storage == "file" -%}
from dotflow.providers import StorageFile
{% elif cookiecutter.storage == "s3" -%}
from dotflow.providers import StorageS3
{% elif cookiecutter.storage == "gcs" -%}
from dotflow.providers import StorageGCS
{% endif -%}
{% if cookiecutter.scheduler == "cron" -%}
from dotflow.providers import SchedulerCron
{% endif %}
from {{ cookiecutter.module_name }}.actions import step_one, step_two

{% if cookiecutter.storage == "default" and cookiecutter.scheduler == "none" -%}
config = Config()
{% elif cookiecutter.storage == "default" and cookiecutter.scheduler == "cron" -%}
config = Config(
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% elif cookiecutter.storage == "file" and cookiecutter.scheduler == "none" -%}
config = Config(storage=StorageFile())
{% elif cookiecutter.storage == "file" and cookiecutter.scheduler == "cron" -%}
config = Config(
    storage=StorageFile(),
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% elif cookiecutter.storage == "s3" and cookiecutter.scheduler == "none" -%}
config = Config(
    storage=StorageS3(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        region="us-east-1",
    )
)
{% elif cookiecutter.storage == "s3" and cookiecutter.scheduler == "cron" -%}
config = Config(
    storage=StorageS3(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        region="us-east-1",
    ),
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% elif cookiecutter.storage == "gcs" and cookiecutter.scheduler == "none" -%}
config = Config(
    storage=StorageGCS(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        project="my-gcp-project",
    )
)
{% elif cookiecutter.storage == "gcs" and cookiecutter.scheduler == "cron" -%}
config = Config(
    storage=StorageGCS(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        project="my-gcp-project",
    ),
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% endif %}

def main():
{%- if cookiecutter.checkpoint == "yes" %}
    workflow = DotFlow(config=config, workflow_id=uuid4())
{%- else %}
    workflow = DotFlow(config=config)
{%- endif %}

    workflow.task.add(step=step_one)
    workflow.task.add(step=step_two)

{%- if cookiecutter.scheduler == "cron" and cookiecutter.checkpoint == "yes" %}
    workflow.schedule(mode="{{ cookiecutter.execution_mode }}", resume=True)
{%- elif cookiecutter.scheduler == "cron" %}
    workflow.schedule(mode="{{ cookiecutter.execution_mode }}")
{%- elif cookiecutter.checkpoint == "yes" %}
    workflow.start(mode="{{ cookiecutter.execution_mode }}", resume=True)
{%- else %}
    workflow.start(mode="{{ cookiecutter.execution_mode }}")
{%- endif %}

    for task in workflow.result_task():
        print(f"Task {task.task_id}: {task.status}")

    return workflow


if __name__ == "__main__":
    main()
