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

# Getting number of lines from first dictionary entry
gly_name = next(iter(fnt_dict))
gly_strc = fnt_dict[gly_name]
line_num = len(gly_strc)

# Calculating box height
box_hgt = fnt_xht / 3

# Calculating bottom line
bottom = -box_hgt * fnt_baseline




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
                           box_hgt	= box_hgt,
                           dsc_hgt  = bottom,
                           syntax   = syntax)

# Exporting the font
fnt.save(os.path.join(out_path, f'{font_name}.ufo'))