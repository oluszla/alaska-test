import json

import requests

from helper import base_url, bear_url


def test_info():
    req = requests.get(f'{base_url}/info')
    assert req.status_code == 200, 'Wrong status'


def test_create_status_code():
    req = requests.post(bear_url, data=json.dumps({"bear_type": 'BLACK', "bear_name": 'bear_name', "bear_age": 10}))
    assert req.status_code == 201, 'Wrong status'


def test_update_status_code(bear_id):
    req = requests.put(f'{bear_url}/{bear_id}', data=json.dumps({"bear_type": 'BLACK', "bear_name": 'bear_name', "bear_age": 16}))
    assert req.status_code == 200, 'Wrong status'


def test_delete_status_code(bear_id):
    req = requests.delete(f'{bear_url}/{bear_id}')
    assert req.status_code == 200, 'Wrong status'


def test_headers():
    req = requests.post(bear_url, data=json.dumps({"bear_type": 'BLACK', "bear_name": 'bear_name', "bear_age": 10}))
    assert req.headers['Date'], 'Header date does not exist'
    assert req.headers['Content-Type'] == 'text/html;charset=utf-8'
    assert req.headers['Transfer-Encoding'] == 'chunked'
    assert req.headers['Server'] == 'Jetty(9.4.z-SNAPSHOT)'


def test_not_found():
    req = requests.get(f'{base_url}/test')
    assert req.status_code == 404, 'Wrong status'
