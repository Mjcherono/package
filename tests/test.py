from mypackage import myModule

def test_top_n():
    # Make sure the top n works correctly
    assert myModule.top_n([8, 3, 5, 2, 7, 4], 3) == [8, 7, 5],"incorrect"