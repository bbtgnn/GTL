# -*- coding: utf-8 -*-

### MODULES
import json
from GTL.classes import Typeface



### VARIABLES
config_path = "/Users/Abbatepaolo/Documents/GitHub/GTL/config.json"



### INSTRUCTIONS
mrg = 233

fnt = Typeface(config_path = config_path)
fnt.render()

fnt.invert()

# Fixing margins
for gly in fnt.rfont:
	if gly.name != "space":
		t0 = int(gly.leftMargin)  - mrg
		gly.leftMargin  = t0
		t1 = int(gly.rightMargin) - mrg
		gly.rightMargin  = t1
		gly.update()

fnt.save_font()