import pytest
import json


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))


def test_calculate_hash(client, app):
    response = client.get('/hash/sha256/foo')
    assert response.status_code == 200
    assert json_of_response(response) == {"data": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"}
