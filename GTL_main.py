# -*- coding: utf-8 -*-

### MODULES

import os

import fontParts.world as fp

import GTL.draw_bits
import GTL.csv_reader

from GTL.shape_functions import *

from GTL_syntax import syntax
from GTL_params import *






### CONSTANTS
UPM = 1000






### INSTRUCTIONS

# Creating the dictionary with all the instructions
fnt_dict = GTL.csv_reader.get_font_from_folder(txt_path)






### DRAWING FONT

# Creating the font
fnt = fp.NewFont(familyName=font_name, styleName=style_name)

# Setting the metrics
fnt.info.unitsPerEm = UPM
fnt.info.descender  = fnt_dsc
fnt.info.xHeight    = fnt_xht
fnt.info.capHeight  = fnt_xht
fnt.info.ascender   = fnt_xht

# Generating the font
GTL.draw_bits.draw_bit_fnt(fnt      = fnt,
                           fnt_dict = fnt_dict,
                           dsc_hgt  = fnt_xht/3,
                           box_size = (fnt_xht/3, fnt_xht/3),
                           syntax   = syntax)

# Exporting the font
fnt.save(os.path.join(out_path, f'{font_name}.ufo'))