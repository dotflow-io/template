import os

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
