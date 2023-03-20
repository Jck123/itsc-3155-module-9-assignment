# TODO: Feature 3
from app import app
import pytest
from flask import request
from flask.testing import FlaskClient


def test_home_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<p class="mb-3">Search for a movie rating below</p>' in response_data

    response = test_app.post('/movies/search', query='Cars')
    response_data = response.data
    assert b'3' in response_data

    response = test_app.post('/movies/search', query='')
    response_data = response.data
    assert b'No entry' in response_data

    response = test_app.post('/movies/search', query='sdfsdfsdfsdf')
    response_data = response.data
    assert b'Movie not found' in response_data
    

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()
