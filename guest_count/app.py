"""Lamda function to interact with dynamoDB and update visitor counts accordingly"""
import json
import logging
import boto3
from CustomEncoder import dec2Float

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = "guestCount"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(dynamodbTableName)


def lambda_handler(event, context):
    """Main lambda function handler"""

    print(f"Event: {event}")
    print(f"Context: {context}")

    guest_id = "guest"

    result = get_count(guest_id)

    if result["body"]:
        current_visitor_count = int(float(result["body"])) + 1
    else:
        current_visitor_count = 1

    response = updateCount(guest_id, current_visitor_count)

    return response


def get_count(guest_id):
    """Retrieve current visitors count from DB"""
    try:
        response = table.get_item(Key={"guest": guest_id})
        if "Item" in response:
            return buildResponse(200, response["Item"]["counts"])
        return buildResponse(404, {"Message": "guest_id: %s not found" % guest_id})
    except Exception as err:
        logger.exception("Unable to retrieve item from table due to: %s", err)


def updateCount(guest_id, current_visitor_count):
    try:
        response = table.update_item(
            Key={"guest": guest_id},
            UpdateExpression="set counts = :value",
            ExpressionAttributeValues={":value": current_visitor_count},
        )
        body = {
            "Operation": "UPDATED",
            "Message": "SUCCESS",
            "count": current_visitor_count,
            "UpdateAttributes": response,
        }
        return buildResponse(200, body)
    except:
        logger.exception(
            "Some custom error handling. Some serious logging going on out here!!"
        )


def buildResponse(statusCode, body=None):

    response = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    }

    if body is not None:
        response["body"] = json.dumps(body, cls=dec2Float)

    return response
