import squares

def test_touch_on_corner():
    one = ((0, 0), (1, 1))
    two = ((1, 1), (2, 2))
    assert overlap.overlap(one, two) == None

