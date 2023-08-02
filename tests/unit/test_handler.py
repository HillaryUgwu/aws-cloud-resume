"""Test for the banckend lambda function"""

import json
import pytest
from src.backend import app

@pytest.fixture()
def count_key():
    """ Generates API GW Event"""
    return "guest"
    
def test_lambda_handler(count_key):
    """Test function handler"""

    result = app.lambda_handler(count_key)
    data = json.loads(result['body'])

    assert data["UpdateAttributes"]["ResponseMetadata"]["HTTPStatusCode"] == 200, "Status code is incorrect"
    assert data["count"], "visitor count data does not exist in the response body"
    assert int(float(data["count"])) >= 0, "Invalid return value"

def test_get_count(count_key):
    """Test get count function"""

    result = app.get_count(count_key)

    assert result["statusCode"] == 200, "Status code is incorrect"
    assert result["body"], "Response does not contain value"
    assert int(float(result["body"])) >= 0, "Invalid return value"

def test_update_count(count_key):
    """Test the update visitors count method"""

    old_result = app.get_count(count_key)
    old_visitor_count = int(float(old_result["body"])) - 1

    response = app.update_count(count_key, old_visitor_count)

    new_result = app.get_count(count_key)

    assert response["statusCode"] == 200, "Status code is incorrect"
    assert "count" in response["body"], "Response does not contain required value"
    assert int(float(new_result["body"])) == int(float(old_result["body"]))-1, "Update not successful"

