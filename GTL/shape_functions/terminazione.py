# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def terminazione(gly, box, rot, tck):

    if rot % 2 == 0:
        rect(gly, box.c)

    contour_operations(gly, box, rot+180)