# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def terminazione(gly, box, rot, tck, *arg):

    # Useful shortcuts
    x, y, w, h = box.c[0], box.c[1], box.w, box.h

    bar_hor = w/2 + tck/2
    bar_ver = h/2 + tck/2
    t = tck/2

    if rot in [0,2]:
        c_x = x
        w = tck
        h = bar_ver

    if rot in [1,3]:
        c_y = y
        w = bar_hor
        h = tck

    # Special casing
    if   rot == 0:
        c_y = y + t - bar_ver/2
    elif rot == 1:
        c_x = x - t + bar_hor/2
    elif rot == 2:
        c_y = y - t + bar_ver/2
    elif rot == 3:
        c_x = x + t - bar_hor/2

    rect(gly, (c_x, c_y), w, h)

    contour_operations(gly)