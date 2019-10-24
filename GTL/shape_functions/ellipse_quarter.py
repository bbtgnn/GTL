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
    sqr = properties["squaring"]
    orn = properties["orientation"]

    # Drawing contour
    pen = gly.getPen()
    pen.moveTo(p0)
    pen.lineTo(p1)
    draw_arc_cw(pen, p1, p2, sqr)
    pen.closePath()

    # Setting right orientation
    c = gly[-1]
    c.scale(orn)

    # Contour operations
    c = gly[-1]
    contour_operations(c, box, properties)