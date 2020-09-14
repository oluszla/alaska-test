from jsonschema import validate

from helper import get_bear_by_id, get_all_bears
from schema import bear_schema


def test_read_specific_bears(bear_id):
    bear = get_bear_by_id(bear_id)
    validate(instance=bear, schema=bear_schema)


def test_read_all_bears(two_bears):
    bears = get_all_bears()
    assert len(bears) == 2
    validate(instance=bears[0], schema=bear_schema)
