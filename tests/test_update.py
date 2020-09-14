import pytest

from helper import update_bear, get_bear_by_id

test_data = [
    ['bear_type', 'POLAR'],  # don't work changing type. By design?
    ['bear_name', 'MASHA'],
    ['bear_age', 15.0]
]


@pytest.mark.parametrize('field_name, field_value', test_data)
def test_update(bear_id, field_name, field_value):
    bear = get_bear_by_id(bear_id)
    bear[field_name] = field_value
    update_bear(bear_id, bear)
    new_bear = get_bear_by_id(bear_id)
    assert new_bear[field_name] == field_value, f'{field_name} was not changed'
