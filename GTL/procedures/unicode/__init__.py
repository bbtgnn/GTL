import os
import fontParts.base as FP
from typing import cast


# CONSTANTS
FILE_CHAR_COMMENT = "#"
FILE_CHAR_SEPARATOR = ";"


# SYSTEM VARIABLES
private_use_count = 0


# UNICODE DICTIONARY CREATION

# Creating empty dictionary that will store unicode values:
#  {"glyph name" : "glyph unicode value (expressed as hex string)"}
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
            key = line_split[1]  # Glyph name
            val = line_split[0]  # Glyph unicode value

            # Value is extracted as string but needs to be converted to hexadecimal
            val = hex(int(val, 16))

            # Updating dictionary
            unicodes_dict[key] = val


# FUNCTIONS

# This function takes a glyph as argument and returns the same glyph with unicode set correctly (hex)

# Glyph -> Glyph
def set_glyph_unicode(glyph: FP.BaseGlyph) -> FP.BaseGlyph:

    global private_use_count
    glyph_name = cast(str, glyph.name)

    # If there's a point in glyph name it means it's a glyph meant for an opentype feature.
    #  These glyphs do not have a unicode value (because they reference the original glyph) so:
    if "." in glyph_name:
        pass

    # If glyph name is in the dictionary
    elif glyph_name in unicodes_dict.keys():
        # We set its unicode value to the matching one
        glyph.unicode = unicodes_dict[glyph_name]

    # If glyph name is in format "uniXXXX"
    elif "uni" in glyph_name:
        glyph.unicode = hex(int(glyph_name.replace("uni", ""), 16))

    # If there's no matching value
    else:
        # We go with private use area
        glyph.unicode = hex(int("F0000", 16) + private_use_count)
        private_use_count += 1
        print(f"Glyph '{
              glyph_name}' not matching any stored Unicode value. Will be assigned to Private Use Area")

    return glyph
