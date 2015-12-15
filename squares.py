def overlap(red, blue):
    """
    Return overlap between two rectangles, or None
    """

    ((red_low_x, red_low_y), (red_hi_x, red_hi_y)) = red
    ((blue_low_x, blue_low_y), (blue_hi_x, blue_hi_y)) = blue

    if (red_low_x >= blue_hi_x) or (red_hi_x <= blue_low_x) or \
       (red_low_y >= blue_hi_x) or (red_hi_y <= blue_low_y):
        return None

    low_x = max(red_low_x, blue_low_x)
    low_y = max(red_low_y, blue_low_y)
    hi_x = min(red_hi_x, blue_hi_x)
    hi_y = min(red_hi_y, blue_hi_y)

    return ((low_x, low_y), (hi_x, hi_y))

