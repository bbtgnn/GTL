# -*- coding: utf-8 -*-



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
    if (p1[0]-p0[0]) * (p1[1]-p0[1]) < 0:
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



# contour_operations
# Scales, rotates, translates the contour according to parameters

# RContour, tuple, dictionary ->
def contour_operations(c, box, properties):

    # Gathering data
    x, y = box[0], box[1]
    scl = properties["scale"]
    rot = properties["rotation"]

    # Applying transformations
    c.scaleBy(scl)
    c.rotateBy(rot)
    c.moveBy((x,y))
    make_counterclockwise(c)
    c.round()
    c.changed()
