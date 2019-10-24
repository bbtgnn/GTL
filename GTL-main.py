# -*- coding: utf-8 -*-

### MODULES

import fontParts.world as fp

import GTL.draw_bits
import GTL.txt_reader

from GTL.shape_functions import *






### VARIABLES

# Path of folder containing glyphs txt
txt_path = "/Users/Abbatepaolo/Documents/GitHub/GTL/test_letters"

# Set glyphs'baseline row (counting from bottom of txt)
gly_baseline = 2

# Set the ratio between width of "pixelone" and its height:
# width_ratio = 2 means the module width will be twice its height
box_ratio = 1

# Set number of "pixelone" sub-units
box_col = 1
box_row = 1






### SYNTAX

sintassi = {

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






### INSTRUCTIONS

# Creating the dictionary with all the instructions
fnt_dict = GTL.txt_reader.get_font_from_folder(txt_path)

# Getting number of lines from first dictionary entry
gly_name = next(iter(fnt_dict))
gly_strc = fnt_dict[gly_name]
line_num = len(gly_strc)

# Calculating box height
box_hgt = 1000/line_num

# Calculating box width
box_wdt = box_hgt * box_ratio

# Calculating descender line
dsc_hgt = -box_hgt * gly_baseline






### DRAWING FONT

fnt = fp.NewFont()

GTL.draw_bits.draw_bit_fnt(fnt = fnt,
                           fnt_dict = fnt_dict,
                           dsc_hgt = dsc_hgt,
                           box_size = (box_wdt, box_hgt),
                           box_layout = (box_row, box_col),
                           syntax = sintassi)

fnt.save("test_font.ufo")