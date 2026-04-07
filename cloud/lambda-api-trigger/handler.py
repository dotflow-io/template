import json

from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked via HTTP POST through API Gateway."""
    body = json.loads(event.get("body", "{}"))
    print(f"Received payload: {body}")

    result = main()
    return {"statusCode": 200, "body": json.dumps({"status": "workflow executed"})}
