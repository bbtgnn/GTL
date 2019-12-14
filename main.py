# -*- coding: utf-8 -*-

### MODULES
import json
from GTL.classes import Typeface



### VARIABLES
config_path = "/Users/Abbatepaolo/Documents/GitHub/GTL/config.json"



### INSTRUCTIONS

fnt = Typeface(config_path = config_path)
fnt.render()

# fnt.invert()

# Fixing margins
for glifo in fnt.glyphs:
	gly = glifo.rglyph
	if gly.leftMargin != None and gly.leftMargin <= 0:
		gly.leftMargin = glifo.font.cell_wdt/2
	if gly.rightMargin != None and gly.rightMargin <= 0:
		gly.rightMargin = glifo.font.cell_wdt/2

fnt.save_font()