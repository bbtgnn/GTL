# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def angolo(gly, box, rot, tck):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2], box[3]
    t = tck/2

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -t    , 0
    p1 =  p0[0], h/2+t
    p2 =  w/2  , p1[1]
    p3 =  p2[0], h/2-t
    p4 =  t    , p3[1]
    p5 =  p4[0], 0

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    for p in [p1, p2, p3]:
        pen.lineTo(p)
    pen.closePath()

    contour_operations(gly, box, rot)