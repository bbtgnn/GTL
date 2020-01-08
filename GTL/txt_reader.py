# -*- coding: utf-8 -*-

### MODULES

import os






### FUNCTIONS

# get_glyph_from_txt
# This function reads a txt file and returns a dictionary entry like this one
# { glyph name : glyph structure }
# { str        : [str]           }

# String -> Dictionary
def get_glyph_from_txt(txt_path):

    # Reading file
    with open(txt_path, "r") as txt_open:

        # Splitting file in separate lines
        txt_lines = txt_open.read().splitlines()

        # Glyph name
        key = txt_lines[0]
        # Glyph structure
        val = txt_lines[2:]

    return {key : val}



# get_font_from_folder
# This function reads all the txts in a folder and returs a dictionary where each entry is a glyph name-structure pair

# String -> Dictionary
def get_font_from_folder(folder_path):

    # Creating an empty dictionary where all the keys will be appended
    font_dict = {}

    # Iterating over folders and subdirectories to get all txt files
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if ".txt" in file:
                # Getting txt path
                txt_path = os.path.join(subdir, file)
                # Adding to the dictionary the key value pair
                font_dict.update(get_glyph_from_txt(txt_path))

    return font_dict
