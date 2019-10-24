# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def ellipse_quarter(gly, box, properties):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2]/2, box[3]/2

    # Points
    p0 = -w, -h
    p1 = -w,  h
    p2 =  w, -h

    # Getting quarter properties
    sqr = set_property(properties["squaring"])

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    pen.lineTo(p1)
    draw_arc_cw(pen, p1, p2, sqr)
    pen.closePath()

    # Setting orientation
    orn = set_property(properties["orientation"])
    if   "N" in orn:
        scl_y =  1
    elif "S" in orn:
        scl_y = -1
    if   "E" in orn:
        scl_x =  1
    elif "W" in orn:
        scl_x = -1
    c = gly[-1]
    c.scaleBy((scl_x, scl_y))

    # Contour operations
    c = gly[-1]
    contour_operations(c, box, properties)