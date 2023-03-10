import pytest
import json
import requests

def get_address(coordinates: list) -> str:
    response = requests.get(
        f'https://api.i-mobility.at/routing/api/v1/nearby_address?latitude={coordinates[1]}&longitude={coordinates[0]}')
    clean_data = json.loads(response.content)
    return clean_data['data']['name']

#Mariahilfer Straße 189, Wien
coordinates = [16.330851, 48.191466]


print(get_address(coordinates))