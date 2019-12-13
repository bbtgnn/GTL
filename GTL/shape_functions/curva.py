# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def curva(gly, box, rot, tck, sqr=.56):

    # Useful shortcuts
    x, y, w, h = box.x, box.y, box.w, box.h
    t = tck/2

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -t    , 0
    p1 =  w/2  , h/2+t
    p2 =  p1[0], h/2-t
    p3 =  t    , 0

    p01 = p0[0], p1[1]
    p23 = p3[0], p2[1]

    m0 = interpolate_points(p0, p01, sqr)
    m1 = interpolate_points(p1, p01, sqr)
    m2 = interpolate_points(p2, p23, sqr)
    m3 = interpolate_points(p3, p23, sqr)


    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    pen.curveTo(m0, m1, p1)
    pen.lineTo(p2)
    pen.curveTo(m2, m3, p3)
    pen.closePath()

    contour_operations(gly, box, rot+90)