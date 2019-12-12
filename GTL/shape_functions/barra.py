# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def barra(gly, box, rot, tck):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2], box[3]

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -tck/2, 0
    p1 =  p0[0], h
    p2 =  tcl/2, p1[1]
    p3 =  p2[0], p0[0]

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    for p in [p1, p2, p3]:
        pen.lineTo(p)
    pen.closePath()

    contour_operations(gly, box, rot)