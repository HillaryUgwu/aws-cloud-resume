# import json

import pytest

from src.backend import app


@pytest.fixture()
def count_key():
    """ Generates API GW Event"""
    return "guest"


def test_lambda_handler(count_key):
    """Test function handler"""

    old_result = app.get_count(count_key)
    current_visitor_count = int(float(old_result["body"])) + 1

    response = app.update_count(count_key, current_visitor_count)

    new_result = app.get_count(count_key)

    assert old_result["statusCode"] == 200
    assert response["statusCode"] == 200
    assert new_result["statusCode"] == 200
    assert "counts" in response["body"]
    assert int(float(old_result["body"])) >= 0
    assert int(float(new_result["body"])) == int(float(old_result["body"]))+1
    # assert int(float(result["body"])) >= 0

def test_get_count(count_key):
    """Test get count function"""

    result = app.get_count(count_key)
    # current_visitor_count = int(float(result["body"])) + 1

    # data = json.loads(result["body"])

    assert result["statusCode"] == 200
    assert "counts" in result["body"]
    assert int(float(result["body"])) >= 0

# def test_update_count(count_key):

#     response = app.update_count(guest_id, current_visitor_count)
#     ret = app.lambda_handler(apigw_event, "")
#     data = json.loads(ret["body"])

#     assert ret["statusCode"] == 200
#     assert "message" in ret["body"]
#     assert data["message"] == "hello world"

