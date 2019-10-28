# -*- coding: utf-8 -*-

### MODULES

import os




### CONSTANTS
FILE_CHAR_COMMENT = "#"
FILE_CHAR_SEPARATOR = ";"



### SYSTEM VARIABLES
private_use_count = 0






### UNICODE DICTIONARY CREATION

# Creating empty dictionary that will store unicode values:
# {"glyph name" : "glyph unicode value (expressed as hex string)"}
unicodes_dict = {}

# Getting reference to the file containing Unicode definitions
module_path = os.path.abspath(os.path.dirname(__file__))
txt_path = os.path.join(module_path, "assets", "aglfn.txt")

# Updating dictionary with definitions from Adobe
with open(txt_path, "r") as txt_file:

    # Extracting single lines from txt
    txt_lines = txt_file.read().splitlines()

    # Iterating over lines:
    for line in txt_lines:

        # Ignoring comments
        if FILE_CHAR_COMMENT not in line:

            # Extracting key and value
            line_split = line.split(FILE_CHAR_SEPARATOR)
            key = line_split[1] # Glyph name
            val = line_split[0] # Glyph unicode value

            # Value is extracted as string but needs to be converted to hexadecimal
            val = hex(int(val, 16))

            # Updating dictionary
            unicodes_dict[key] = val






### FUNCTIONS

# This function takes a glyph as argument and returns its unicode value (hex)

# Glyph -> Hex
def set_unicode(gly):

    global private_use_count

    # If there's a point in glyph name it means it's a glyph regarding an opentype feature. These glyphs do not use a unicode value, because they reference the original glyph, so:
    if "." in gly.name:
        pass

    # If glyph name is in the dictionary
    elif gly.name in unicodes_dict.keys():
        # We set its unicode value to the matching one
        gly.unicode = unicodes_dict[gly.name]

    # If glyph name is in format "uniXXXX"
    elif "uni" in gly.name:
        gly.unicode = hex(int(gly.name.replace("uni", ""), 16))

    # If there's no matching value
    else:
        # We go with private use area
        gly.unicode = hex(int("F0000", 16) + private_use_count)
        private_use_count += 1
        print(f"Glyph '{gly.name}' not matching any stored Unicode value. Will be assigned to Private Use Area")

    return gly