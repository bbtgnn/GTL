# -*- coding: utf-8 -*-
from ._utilities import *
from random import choice



# RGlyph, tuple(float, 4), list
def random_function (gly, box, properties):

    # Function name (type: function)
    function, properties = choice(properties)

    # Running function
    function(gly=gly, box=box, properties=properties)
