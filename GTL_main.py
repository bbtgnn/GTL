# -*- coding: utf-8 -*-

### MODULES

import os
import pathlib

# Getting modules path
gtl_path = pathlib.Path(__file__).parent.absolute()
modules_path = os.path.join(gtl_path, "GTL", "modules")

# Importing fontParts
import sys
sys.path.append(modules_path)
from fontParts import world as fp

# Importing GTL
import GTL.draw_bits
import GTL.txt_reader
from GTL.shape_functions import *
from GTL_syntax import syntax
from GTL_params import *






### CONSTANTS
UPM = 1000






### INSTRUCTIONS

# Creating the dictionary with all the instructions
fnt_dict = GTL.txt_reader.get_font_from_folder(txt_path)

# Getting number of lines from first dictionary entry
gly_name = next(iter(fnt_dict))
gly_strc = fnt_dict[gly_name]
line_num = len(gly_strc)

# Calculating box height
box_hgt = int(UPM/line_num/4)*4

# Calculating box width
box_wdt = box_hgt * width_ratio

# Calculating bottom line
bottom = -box_hgt * fnt_baseline

box = box_wdt, box_hgt




### DRAWING FONT

# Creating the font
fnt = fp.NewFont(familyName=font_name, styleName=style_name)

# Setting the metrics
fnt.info.unitsPerEm = UPM
fnt.info.descender  = - box_hgt * fnt_dsc
fnt.info.xHeight    =   box_hgt * fnt_xht
fnt.info.capHeight  =   box_hgt * fnt_cap
fnt.info.ascender   =   box_hgt * fnt_asc

# Generating the font
GTL.draw_bits.draw_bit_fnt(fnt        = fnt,
                           fnt_dict   = fnt_dict,
                           dsc_hgt    = bottom,    # this is actually the bottom line
                           box_size   = box,
                           box_layout = box_layout,
                           syntax     = syntax)

# Exporting the font
fnt.save(os.path.join(out_path, f'{font_name}.ufo'))