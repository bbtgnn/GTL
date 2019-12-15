# -*- coding: utf-8 -*-
from ._utilities import *
from .barra import *
from .terminazione import *


# RGlyph, tuple(float, 4), dict ->
def innesto(gly, box, rot, tck, *arg):

    # Useful shortcuts
    x, y, w, h = box.c[0], box.c[1], box.w, box.h
    t = tck/2

    barra(gly, box, rot, tck)
    contour_operations(gly)
    rot = [1, 0, 3, 2][rot]
    terminazione(gly, box, rot, tck)
    contour_operations(gly)
