# -*- coding: utf-8 -*-
import random
import types



# interpolate_points
# Interpolation of two tuples

def interpolate_values(pA, pB, f):
    v = pA+(pB-pA)*f
    return v

# tuple, tuple, float -> tuple
def interpolate_points(pA, pB, f):
    return tuple([pA[i]+(pB[i]-pA[i])*f for i in (0,1)])






# contour_operations
def contour_operations(gly):
    c = gly[-1]
    # Making anticlockwise
    if c.clockwise == True:
        c.reverse()
    c.round()
    c.changed()



# Rect
def rect(gly, c, w, h):

    # Points
    p0 = c[0]  - w/2, c[1]  - h/2
    p1 = p0[0]      , p0[1] + h
    p2 = p0[0] + w  , p1[1]
    p3 = p2[0]      , p0[1]

    # Drawing
    pen = gly.getPen()
    pen.moveTo(p0)
    pen.lineTo(p1)
    pen.lineTo(p2)
    pen.lineTo(p3)
    pen.closePath()
