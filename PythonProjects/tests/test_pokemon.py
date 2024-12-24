import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b190b348ab32a0fe317581337a612e49'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '23159'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers')
    assert response.status_code == 200
 
 
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()