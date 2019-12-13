# -*- coding: utf-8 -*-
from ._utilities import *



# Barra
def barra(gly, box, rot, tck):

    # Drawing rectangle
    if rot % 2 == 0:
        rect(gly, box.c, tck, box.h)
    else:
        rect(gly, box.c, box.w, tck)

    #contour_operations(gly)