import pytest

from helper import create_bear, get_bear_by_id, create_request

test_data = [
    ['BLACK', 'GRIZZLY', 0],
    ['POLAR', 'White', 12.6],
    ['GUMMY', 'mummy', 9.0],
    ['BLACK', '测试', 100.0],
    ['BLACK', 1, 100.0],
    ['BLACK', ' ', 100.0],
    ['BLACK', 'test test', 100.0],
    ['BLACK', '', 100.0],
    ['BLACK', '~!@#$%^&*()_+=-":>?<}{[],./|\\', 100.0],
    ['BLACK', '1' * 1000, 100.0]
]


@pytest.mark.parametrize('bear_type, bear_name, bear_age', test_data)
def test_create_bear(bear_type: str, bear_name: str, bear_age: float):
    bear_id = create_bear(bear_type, bear_name, bear_age)
    bear = get_bear_by_id(bear_id)
    assert bear['bear_type'] == bear_type
    assert bear['bear_name'] == str(bear_name).upper()  # why does service make names upper?
    assert bear['bear_age'] == bear_age


@pytest.mark.parametrize('bear_age', [-1, 100.1])
def test_create_age(bear_age):
    bear_id = create_bear('POLAR', 'test', bear_age)
    bear = get_bear_by_id(bear_id)
    assert bear['bear_age'] == 0.0  # why 0.0?


def test_create_wrong_bear_type():
    req = create_request('brown', 'test', 10)
    assert req.status_code == 500  # by design or bug ?
