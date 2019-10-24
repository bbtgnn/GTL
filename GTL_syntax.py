# -*- coding: utf-8 -*-
from GTL.shape_functions import *



### CONSTANTS
ORIENTATIONS = ["NW", "NE", "SW", "SE"]






### PROPERTIES

p_do_nothing = {
    "null": "null"
    }


p_rectangle = {
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0
    }


p_ellipse = {
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0,
    "squaring": .56
    }


p_ellipse_quarter = {
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0,
    "squaring": .56,
    "orientation": "NE"
}


p_rhombus = {
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0,
    "squaring": 0
    }


p_triangle = {
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0,
    "squaring": 0,
    "orientation": "NE",
}


p_random_function = [
    (rectangle      , p_rectangle      ),
    (ellipse        , p_ellipse      ),
    (ellipse_quarter, p_ellipse_quarter),
    (ellipse        , p_rhombus),
    (ellipse_quarter, p_triangle),
]






### SYNTAX

syntax = {
    ".": (do_nothing, p_do_nothing),
    "#": (random_function, p_random_function),
}