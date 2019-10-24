# -*- coding: utf-8 -*-
from GTL.shape_functions import *






### SYNTAX

syntax = {

    ".": (do_nothing,
          {
          "null": "null"
          }),

    "#": (rectangle,
          {
           "scale": 1,
           "rotation": 45
          }),
}