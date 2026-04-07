from {{MODULE_NAME}}.workflow import main


def handler(event, context):
    """Invoked when a file is uploaded to the S3 source bucket."""
    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        print(f"Processing s3://{bucket}/{key}")

    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
