# -*- coding: utf-8 -*-

### MODULES

import fontParts.world as fp

import GTL.draw_bits
import GTL.txt_reader

from GTL.shape_functions import *

from GTL_syntax import syntax






### VARIABLES

# Path of folder containing glyphs txt
txt_path = "/Users/Abbatepaolo/Documents/GitHub/GTL/test_letters"

# Path of output font
out_path = "/Users/Abbatepaolo/Desktop/test_font.ufo"

# Set glyphs'baseline row (counting from bottom of txt)
gly_baseline = 2

# Set box size
box = 100, 100

# Set number of "pixelone" sub-units
box_col = 1
box_row = 1






### INSTRUCTIONS

# Creating the dictionary with all the instructions
fnt_dict = GTL.txt_reader.get_font_from_folder(txt_path)

# Getting number of lines from first dictionary entry
gly_name = next(iter(fnt_dict))
gly_strc = fnt_dict[gly_name]
line_num = len(gly_strc)

# Calculating descender line
dsc_hgt = -box[1] * gly_baseline






### DRAWING FONT

fnt = fp.NewFont()

GTL.draw_bits.draw_bit_fnt(fnt = fnt,
                           fnt_dict = fnt_dict,
                           dsc_hgt = dsc_hgt,
                           box_size = box,
                           box_layout = (box_row, box_col),
                           syntax = syntax)

fnt.save(out_path)