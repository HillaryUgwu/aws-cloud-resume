#! /home/gitpod/.pyenv/shims/python

"""Lamda function to interact with dynamoDB and update visitor counts accordingly"""
import json
import logging
import boto3
from CustomEncoder import dec2Float

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = "cloud-resume-challenge"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(dynamodbTableName)


def lambda_handler(event, context):
    """Main lambda function handler"""

    guest_id = "guest"

    result = get_count(guest_id)
    current_visitor_count = int(float(result["body"])) + 1

    response = update_count(guest_id, current_visitor_count)

    return response


def get_count(guest_id):
    """Retrieve current visitors count from DB"""
    try:
        response = table.get_item(Key={"guest_id": guest_id})
        if "Item" in response:
            return build_response(200, response["Item"]["counts"])
        return build_response(200, 0)
    except Exception as err:
        logger.exception("Unable to retrieve item from table due to: %s", err)


def update_count(guest_id, current_visitor_count):
    """Update DB with the current visitors count"""
    try:
        response = table.update_item(
            Key={"guest_id": guest_id},
            UpdateExpression="set counts = :value",
            ExpressionAttributeValues={":value": current_visitor_count},
        )
        body = {
            "Operation": "UPDATED",
            "Message": "SUCCESS",
            "count": current_visitor_count,
            "UpdateAttributes": response,
        }
        return build_response(200, body)
    except Exception as err:
        logger.exception("Unable to update the table due to: %s", err)


def build_response(status_code, body=None):
    """Build custom response for specific requests"""

    response = {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    }

    if body is not None:
        response["body"] = json.dumps(body, cls=dec2Float)

    return response
