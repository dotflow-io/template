import os
import json

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked via HTTP POST through API Gateway."""
    body = json.loads(event.get("body", "{}"))
    print(f"Received payload: {body}")

    result = main()
    return {"statusCode": 200, "body": json.dumps({"status": "workflow executed"})}
