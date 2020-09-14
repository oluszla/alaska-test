import pytest

from helper import create_bear, delete_all_bears


@pytest.fixture(autouse=True)
def clear():
    yield
    delete_all_bears()


@pytest.fixture(scope="function")
def bear_id():
    yield create_bear('BLACK', 'test', 10)


@pytest.fixture(scope='function')
def two_bears():
    first_id = create_bear('BLACK', 'first', 25)
    second_id = create_bear('POLAR', 'second', 30)
    yield first_id, second_id
