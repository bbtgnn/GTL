# -*- coding: utf-8 -*-

### MODULES

import os
import csv






### FUNCTIONS

# get_glyph_from_txt
# This function reads a txt file and returns a dictionary entry like this one
# { glyph name : glyph structure }
# { str        : [str]           }

# String -> Dictionary
def get_glyph_from_csv(csv_path):

    # Reading file
    with open(csv_path, "r") as csv_open:

        csv_reader = csv.reader(csv_open)

        gly_structure = []
        for line in csv_reader:
            gly_structure.append(line)

        gly_name = os.path.basename(csv_path).split(".csv")[0]

    return {gly_name : gly_structure}



# get_font_from_folder
# This function reads all the txts in a folder and returs a dictionary where each entry is a glyph name-structure pair

# String -> Dictionary
def get_font_from_folder(folder_path):

    # Creating an empty dictionary where all the keys will be appended
    font_dict = {}

    # Iterating over folders and subdirectories to get all txt files
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if ".csv" in file:
                # Getting txt path
                txt_path = os.path.join(subdir, file)
                # Adding to the dictionary the key value pair
                font_dict.update(get_glyph_from_csv(txt_path))

    return font_dict
