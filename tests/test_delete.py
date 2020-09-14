from helper import delete_bear_by_id, get_all_bears, delete_all_bears


def test_delete_one_bear(two_bears):
    delete_bear_by_id(two_bears[0])
    bears = get_all_bears()
    assert len(bears) == 1, 'Bear was not deleted'
    assert bears[0]['bear_id'] == two_bears[1], 'Deleted wrong bear'


def test_delete_all_bears(two_bears):
    delete_all_bears()
    bears = get_all_bears()
    assert len(bears) == 0, 'Bears was not deleted'
