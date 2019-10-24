# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def rectangle(gly, box, properties):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2]/2, box[3]/2

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -w, -h
    p1 = -w,  h
    p2 =  w,  h
    p3 =  w, -h

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    for p in [p1, p2, p3]:
        pen.lineTo(p)
    pen.closePath()

    # Contour operations
    c = gly[-1]
    contour_operations(c, box, properties)