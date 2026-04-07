from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked by EventBridge on a schedule."""
    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
