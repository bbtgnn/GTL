# -*- coding: utf-8 -*-
from ._utilities import *
from math import atan, cos



# 
def diagonale(gly, box, rot, tck, *arg):

    t = tck/2

    apt_hor_inr = box.c[0] - t, box.y
    apt_hor_otr = box.c[0] + t, box.y
    apt_ver_inr = box.x       , box.c[1] - t
    apt_ver_otr = box.x       , box.c[1] + t

    # Some geometry
    a = apt_hor_inr[0] - box.x
    b = apt_ver_inr[1] - box.y

    m = -b/a
    β = atan(m)
    q = b + tck/cos(β)

    y = lambda x: m * x + q
    xH = a + tck
    yH = y(xH)

    x = lambda y: (y - q) / m
    yV = b + tck
    xV = x(yV)

    apt_ver_upr = box.x + xV, box.y + yV
    apt_hor_upr = box.x + xH, box.y + yH


    pen = gly.getPen()
    pen.moveTo(apt_hor_inr)
    for p in [apt_ver_inr, apt_ver_otr, apt_ver_upr, apt_hor_upr, apt_hor_otr]:
        pen.lineTo(p)
    pen.closePath()


    tx, ty =  1,  1
    if rot == 1:
        tx, ty = -1,  1
    if rot == 2:
        tx, ty = -1, -1
    if rot == 3:
        tx, ty = 1 , -1
    gly[-1].scaleBy((tx, ty), origin=box.c)
    contour_operations(gly)
