# -*- coding: utf-8 -*-

### MODULES

from GTL.set_unicode import *






### FUNCTIONS

# draw_bit_chr
# This function reads a character at a given position
# and creates a virtual box that gets divided into nxm (box_layout) cells.
# For each cell, a drawing function specified in the syntax dictionary gets executed.

# RGlyph, string, (float, float), (float, float), (int, int), dictionary
def draw_bit_chr(gly, char, box, syntax):

    if char in syntax.keys():
        function   = syntax[char][0]
        properties = syntax[char][1]

        function(gly=gly, box=box, properties=properties)

    else:
        print(f"There's an invalid character used ({char}) in glyph {gly.name}. Please check glyph txt file or add the corresponding rule in the syntax.")



# draw_bit_lin
# This function iterates draw_bit_chr over a string (line) of characters.

# RGlyph, string, (float, float), (float, float), (int, int), dictionary
def draw_bit_lin(gly, char_line, box, syntax):

    # Unpacking
    box_x, box_y, box_w, box_h = box

    for char in char_line:
        draw_bit_chr(gly, char, box, syntax)

        # Translating the x position by the width of the box
        box_x += box_w



# draw_bit_gly
# This function iterates draw_bit_lin over the full glyph ascii description.
# (So it draws the full glyph)

# RGlyph, list of lists, float, (float, float), (int, int), dictionary -> RGlyph
def draw_bit_gly(gly, gly_desc, dsc_hgt, box_size, syntax):

    # Setting starting coordinates
    box_x = 0
    box_y = dsc_hgt    # We start from the descender, then we go all the way up

    # Iterating over glyph instructions (but backwards, so that we start from the descenders)
    for char_line in gly_desc[::-1]:
        draw_bit_lin(gly, char_line, (box_x, box_y, *box_size), syntax)

        # Updating position once a row of characters (lin) is completed
        box_x = 0
        box_y += box_size[1]

    return gly



# draw_bit_fnt
# This function generates a full set of *alternative* (alt) glyphs from instructions.

# RFont, dictionary, string, float, (float, float), (int, int), dictionary -> RFont
def draw_bit_fnt(fnt, fnt_dict, dsc_hgt, box_size, syntax):

    # Iterating over the dictionary (the instructions)
    for gly_name in fnt_dict.keys():

        # Creating new glyph
        gly = fnt.newGlyph(gly_name)
        set_unicode(gly)
        gly.clear()

        # Getting glyph description from dict
        gly_desc = fnt_dict[gly_name]

        # Setting glyph width
        gly.width = box_size[0] * len(gly_desc[0])

        # Drawing the glyph
        draw_bit_gly(gly, gly_desc, dsc_hgt, box_size, syntax)

    return fnt