# -*- coding: utf-8 -*-

### MODULES
import json
from GTL.classes import Typeface



### VARIABLES
config_path = "/Users/Abbatepaolo/Documents/GitHub/GTL/config.json"



### INSTRUCTIONS
fnt = Typeface(config_path = config_path)
fnt.render()
fnt.save_font()