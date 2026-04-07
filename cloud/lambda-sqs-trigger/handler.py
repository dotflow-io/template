import json

from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked when a message arrives in the SQS queue."""
    for record in event.get("Records", []):
        body = json.loads(record["body"])
        print(f"Processing message: {body}")

    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
