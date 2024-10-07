import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():

    #arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    #act
    response = requests.get(url)
    body = response.json()

    #asser
    assert response.status_code == 200
    assert 'Python' in body['AbstractText']