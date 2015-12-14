function overlap, red, blue
  ;+
  ; Return overlap between two rectangles or -1
  ;-
  red_low_x = red[0]
  red_low_y = red[1]
  red_hi_x = red[2]
  red_hi_y = red[3]

  blue_low_x = blue[0]
  blue_low_y = blue[1]
  blue_hi_x = blue[2]
  blue_hi_y = blue[3]

  if (red_low_x ge blue_hi_x) or (red_hi_x le blue_low_x) or $
     (red_low_y ge blue_hi_x) or (red_hi_y le blue_low_y) then return, -1

  low_x = max([red_low_x, blue_low_x])
  low_y = max([red_low_y, blue_low_y])
  hi_x = min([red_hi_x, blue_hi_x])
  hi_y = min([red_hi_y, blue_hi_y])
  
  return, [low_x, low_y, hi_x, hi_y]
  end
