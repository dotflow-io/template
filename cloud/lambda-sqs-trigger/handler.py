import os
import json

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked by SQS messages."""
    for record in event.get("Records", []):
        body = json.loads(record.get("body", "{}"))
        print(f"Received message: {body}")

    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
