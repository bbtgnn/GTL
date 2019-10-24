# -*- coding: utf-8 -*-
import random
import types



# interpolate_points
# Interpolation of two tuples

# tuple, tuple, float -> tuple
def interpolate_points(pA, pB, f):
    return tuple([pA[i]+(pB[i]-pA[i])*f for i in (0,1)])



# draw_arc
# Draws a clockwise arc between two points given squaring

# tuple, tuple, tuple, float ->
def draw_arc_cw(pen, p0, p1, s):

    # Determining the maximum point
    if (p1[0]-p0[0]) * (p1[1]-p0[1]) > 0:
        pM = p0[0], p1[1]
    else:
        pM = p1[0], p0[1]

    # Calculating mid interpolated points
    pI = [interpolate_points(p, pM, s) for p in (p0, p1)]

    # Drawing curve
    pen.curveTo(pI[0], pI[1], p1)



# make_counterclockwise
# Makes a contour counterclockwise

# RContour -> RContour
def make_counterclockwise(c):

    if c.clockwise == True:
        c.reverse()

    return c



# set_property
# sets function property according to format
def set_property(p):

    if (type(p) is int) or (type(p) is float) or (type(p) is str):
        return p

    elif (type(p) is tuple):

        if   p[0] == "RANGE":
            return random.uniform(*p[1])

        elif p[0] == "CHOICE":
            return random.choice(p[1])

    else:
        pass



# contour_operations
# Scales, rotates, translates the contour according to parameters

# RContour, tuple, dictionary ->
def contour_operations(c, box, properties):

    # Gathering data
    x, y = box[0], box[1]
    scl_x = set_property(properties["scale_x"])
    scl_y = set_property(properties["scale_y"])
    rot = set_property(properties["rotation"])

    # Applying transformations
    c.scaleBy((scl_x, scl_y))
    c.rotateBy(rot)
    c.moveBy((x,y))
    make_counterclockwise(c)
    c.round()
    c.changed()
