# -*- coding: utf-8 -*-

### MODULES

import os

import fontParts.world as fp

from GTL.classes import Typeface, Glyph, Cell

from GTL.shape_functions import *

from GTL_syntax import syntax
from GTL_params import *






### CONSTANTS
UPM = 1000

csv_path = "/Users/Abbatepaolo/Documents/GitHub/GTL/csv_letters"










### DRAWING FONT

# Creating the font
fnt = Typeface(family_name="retorica", wh=(100,100))

# # Setting the metrics
# fnt.info.unitsPerEm = UPM
# fnt.info.descender  = fnt_dsc
# fnt.info.xHeight    = fnt_xht
# fnt.info.capHeight  = fnt_xht
# fnt.info.ascender   = fnt_xht

# # Generating the font
# GTL.draw_bits.draw_bit_fnt(fnt      = fnt,
#                            fnt_dict = fnt_dict,
#                            dsc_hgt  = fnt_xht/3,
#                            box_size = (fnt_xht/3, fnt_xht/3),
#                            syntax   = syntax)


fnt.generate_glyphs(csv_path)
fnt.render()
fnt.add_space(2)
fnt.save_font("/Users/Abbatepaolo/Documents/GitHub/GTL")