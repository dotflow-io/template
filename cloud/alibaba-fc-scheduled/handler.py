import os

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked by Timer Trigger on a schedule."""
    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
