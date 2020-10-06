import asyncio

from run import app
from starlette.testclient import TestClient

client = TestClient(app)
loop = asyncio.get_event_loop()


def test_token_successful():
    response = client.post('/login', dict(username='test', password='test'))

    assert response.status_code == 200, 'Get access token response is 200'
    assert "access_token" in response.json(), 'Token is received'


def test_get_category(categories_array=None):
    if categories_array is None:
        categories_array = ['food', 'learning', 'art', 'sport', 'party', 'friends', 'travel']
    for category in categories_array:
        response = client.get(f'/v1/{category}')
        assert response.status_code == 200, f'Get {category} page loaded successfully'
