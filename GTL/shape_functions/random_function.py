# -*- coding: utf-8 -*-
from ._utilities import *
from random import choice



# RGlyph, tuple(float, 4), list
def random_function (gly, box, properties):

    lst = properties["function_properties_list"]

    # Function name (type: function)
    function, properties = choice(lst)

    # Running function
    function(gly=gly, box=box, properties=properties)
