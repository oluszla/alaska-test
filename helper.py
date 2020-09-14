import json

import requests

base_url = 'http://0.0.0.0:8091'
bear_url = f'{base_url}/bear'


def create_bear(bear_type: str = None, bear_name: str = None, bear_age: float = None) -> int:
    bear = {"bear_type": bear_type, "bear_name": bear_name, "bear_age": bear_age}
    req = requests.post(bear_url, data=json.dumps(bear))
    bear_id = int(req.content)
    return bear_id


def create_request(bear_type: str = None, bear_name: str = None, bear_age: float = None):
    bear = {"bear_type": bear_type, "bear_name": bear_name, "bear_age": bear_age}
    req = requests.post(bear_url, data=json.dumps(bear))
    return req


def get_bear_by_id(bear_id: int = None) -> dict:
    req = requests.get(f'{bear_url}/{bear_id}')
    return json.loads(req.content)


def get_all_bears() -> dict:
    req = requests.get(bear_url)
    return json.loads(req.content)


def update_bear(bear_id, bear: dict):
    requests.put(f'{bear_url}/{bear_id}', data=json.dumps(bear))


def delete_all_bears():
    requests.delete(f'{bear_url}')


def delete_bear_by_id(bear_id: int):
    requests.delete(f'{bear_url}/{bear_id}')
