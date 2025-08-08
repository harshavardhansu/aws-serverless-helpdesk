import json
import os
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("TABLE_NAME")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    # Expect POST via API Gateway with JSON body
    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)
        title = body.get("title", "No title")
        description = body.get("description", "")
        user = body.get("user", "anonymous")

        ticket_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        item = {
            "ticketId": ticket_id,
            "title": title,
            "description": description,
            "user": user,
            "status": "OPEN",
            "createdAt": now
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"ticketId": ticket_id, "message": "Ticket created", "item": item})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
