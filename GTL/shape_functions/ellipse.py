# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def ellipse(gly, box, properties):

    # Useful shortcut
    x, y, w, h = box[0], box[1], box[2]/2, box[3]/2

    # Points (ideally, we draw at (0,0), then we translate)
    p0 = -w, 0
    p1 =  0, h

    # Drawing arcs
    pen = gly.getPen()
    pen.moveTo(p0)

    # Getting ellipse squaring
    sqr = properties["squaring"]

    for i in range(4):

        draw_arc_cw(pen, p0, p1, sqr)

        # Calculating next points
        p_tmp = [-i for i in p0]
        p0 = p1
        p1 = tuple(p_tmp)

    pen.closePath()

    # Contour operations
    c = gly[-1]
    contour_operations(c, box, properties)