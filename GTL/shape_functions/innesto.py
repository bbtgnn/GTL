# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def barra(gly, box, rot, tck):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2], box[3]
    t = tck/2

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -t    , 0
    p1 =  p0[0], h
    p2 =  t    , p1[1]
    p3 =  p2[0], h/2+t
    p4 =  w/2  , p3[1]
    p5 =  p4[0], h/2-t
    p6 =  t    , p5[1]
    p7 =  t    , 0

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    for p in [p1, p2, p3, p4, p5, p6, p7]:
        pen.lineTo(p)
    pen.closePath()

    contour_operations(gly, box, rot)