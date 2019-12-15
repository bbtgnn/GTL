# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def angolo(gly, box, rot, tck, *arg):

    # Useful shortcuts
    x, y, w, h = box.c[0], box.c[1], box.w, box.h

    bar_hor = w/2 + tck/2
    bar_ver = h/2 + tck/2

    if   rot in [0,3]:
        c_hor_x = x - w/2 + bar_hor/2
    elif rot in [1,2]:
        c_hor_x = x + w/2 - bar_hor/2
    c_hor_y = box.c[1]

    c_ver_x = box.c[0]
    if   rot in [0,1]:
        c_ver_y = y - h/2 + bar_ver/2
    elif rot in [2,3]:
        c_ver_y = y + h/2 - bar_ver/2

    rect(gly, (c_hor_x,c_hor_y), bar_hor, tck)
    contour_operations(gly)
    rect(gly, (c_ver_x,c_ver_y), tck, bar_ver)
    contour_operations(gly)