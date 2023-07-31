import requests
import pytest

token = '53e6b3cb721ec006b71a55b6fe72bf75'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_status_name():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : '1898'})
    assert response.json()['trainer_name'] == 'dfbdfg'
