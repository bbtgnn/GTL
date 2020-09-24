# -*- coding: utf-8 -*-
from GTL.shape_functions import *



### CONSTANTS
ORIENTATIONS = ["NW", "NE", "SW", "SE"]



### PROPERTIES

# do_nothing
p_do_nothing = {
    "null": "null"
}

# rectangle
p_rectangle = {
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0,
}

# right triangle = a quarter of ellipse with zero squaring (Possible orientations: NE, NW, SE, SW)
p_ellipse_quarter = {
    "orientation": "NW",
    "scale_x": 1,
    "scale_y": 1,
    "rotation": 0,
    "squaring": 0.56
}

## EXTRAS 2 - Ready-made corners

p_ellipse_quarter_NW = p_ellipse_quarter.copy()
p_ellipse_quarter_NW["orientation"] = "NW"

p_ellipse_quarter_NE = p_ellipse_quarter.copy()
p_ellipse_quarter_NE["orientation"] = "NE"

p_ellipse_quarter_SW = p_ellipse_quarter.copy()
p_ellipse_quarter_SW["orientation"] = "SW"

p_ellipse_quarter_SE = p_ellipse_quarter.copy()
p_ellipse_quarter_SE["orientation"] = "SE"



### SYNTAX

syntax = {
    # Do nothing
    ".": (do_nothing, p_do_nothing),
    # Main structure
    "#": (rectangle, p_rectangle),
    # Corners
    "0": (ellipse_quarter, p_ellipse_quarter_NW),
    "1": (ellipse_quarter, p_ellipse_quarter_NE),
    "2": (ellipse_quarter, p_ellipse_quarter_SW),
    "3": (ellipse_quarter, p_ellipse_quarter_SE)
}