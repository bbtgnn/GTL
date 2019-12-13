# -*- coding: utf-8 -*-
from ._utilities import *



# RGlyph, tuple(float, 4), dict ->
def curva(gly, box, rot, tck, sqr=.56):

    # Drawing
    pen = gly.getPen()

    for f in (1,-1):

        apt_hor = box.c[0] + f*tck/2, box.y
        apt_ver = box.x             , box.c[1] + f*tck/2

        cpt = apt_hor[0], apt_ver[1]

        cpt_hor = interpolate_points(apt_hor, cpt, sqr)
        cpt_ver = interpolate_points(apt_ver, cpt, sqr)

        bpt_lst = [apt_hor, cpt_hor, cpt_ver, apt_ver]

        l = bpt_lst
        l = l[::f]

        if f == 1:
            pen.moveTo(l[0])
        if f == -1:
            pen.lineTo(l[0])
        pen.curveTo(l[1], l[2], l[3])

    pen.closePath()
    if rot == 0:
        tx, ty =  1,  1
    if rot == 1:
        tx, ty = -1,  1
    if rot == 2:
        tx, ty = -1, -1
    if rot == 3:
        tx, ty = 1 , -1
    gly[-1].scaleBy((tx, ty), origin=box.c)
    contour_operations(gly)

















