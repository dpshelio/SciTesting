from squares import overlap

def test_touch_on_corner():
    one = ((0, 0), (1, 1))
    two = ((1, 1), (2, 2))
    assert overlap(one, two) == None

