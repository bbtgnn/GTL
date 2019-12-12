# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def curva(gly, box, rot, tck, sqr):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2], box[3]
    t = tck/2

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -t    , 0
    p1 =  w/2  , h/2+t
    p2 =  p1[0], h/2-t
    p3 =  t    , 0

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    draw_arc_cw(pen, p0, p1, s)
    pen.lineTo()
    draw_arc_cw(pen, p2, p3, s)
    pen.closePath()

    contour_operations(gly, box, rot)