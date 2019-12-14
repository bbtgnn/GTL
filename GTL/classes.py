### MODULES

import os
import csv
import json

from pathlib import Path
import fontParts.world as fp

from GTL.shape_functions._utilities import interpolate_values, rect

from GTL.shape_functions.angolo import angolo
from GTL.shape_functions.curva import curva
from GTL.shape_functions.barra import barra
from GTL.shape_functions.innesto import innesto
from GTL.shape_functions.terminazione import terminazione
from GTL.shape_functions.diagonale import diagonale
from GTL.shape_functions.vuoto import vuoto
from GTL.shape_functions.v import v



### SYNTAX

sintassi = {
	"A": angolo,
	"C": curva,
	"B": barra,
	"I": innesto,
	"T": terminazione,
	"D": diagonale,
	"V": v,
	"0": vuoto
}




### CLASSES


class Box:

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.c = x+w/2, y+h/2



class Typeface:

	UPM = 1000

	def __init__(self, config_path):

		config_path = Path(config_path)
		self.config = json.loads(config_path.read_text())

		self.path = Path(self.config['path_csv_glyphs'])
		self.family = self.config['font_name']
		self.rfont = fp.NewFont(familyName=self.family, styleName=self.config['style_name'])
		self.__setup()
		self.glyphs = []
		self.__generate_glyphs()


	def __setup(self):

		base = 12
		self.cell_hgt = base * round(self.UPM / self.config["line_num"] / base)
		self.cell_wdt = self.cell_hgt * self.config["size_ratio"]
		self.size = self.cell_wdt, self.cell_hgt

		self.tck = self.config["tck"]
		self.tck_min = self.config["tck_min"]
		self.sqr = self.config["sqr"]
		self.exp = self.config["exp"]
		self.inv = self.config["inv"]
		self.expansion_factor = self.config["expansion_factor"]

		self.rfont.info.unitsPerEm = self.UPM
		metrics = self.config["font_metrics"]

		self.rfont.info.descender 	= - metrics['fnt_dsc'] * self.cell_hgt
		self.rfont.info.xHeight 	=   metrics['fnt_xht'] * self.cell_hgt
		self.rfont.info.capHeight 	=   metrics['fnt_cap'] * self.cell_hgt
		self.rfont.info.ascender 	=   metrics['fnt_asc'] * self.cell_hgt


	def __generate_glyphs(self):
		csv_list = Path(self.path).glob("**/*.csv")
		for csv_file in csv_list:
			gly = Glyph(self, csv_file)
			self.glyphs.append(gly)


	def render(self):
		for glyph in self.glyphs:
			glyph.render()


	def save_font(self):
		path = Path(f'{self.family}.ufo')
		self.rfont.save(str(path))


	def invert(self):
		for glyph in self.glyphs:
			gly = glyph.rglyph
			gly.removeOverlap()
			for row in glyph.cells:
				for cell in row:
					print(cell.box.x, cell.box.w, glyph.width)
					if cell.box.x + cell.box.w > glyph.width:
						pass
					else:
						rect(gly, cell.box.c, cell.box.w, cell.box.h)



class Glyph:

	def __init__(self, font, path):
		self.font = font
		self.path = path
		self.name = self.path.name[:-4]
		self.cells = []
		self.__carica_celle()

		self.width = self.__get_width()

		self.rglyph = self.font.rfont.newGlyph(self.name)
		self.rglyph.width = self.__get_width()
		self.__set_unicode_name()


	def __set_unicode_name(self):

		if "." in self.name:
			pass

		else:
			aglfn = Path("GTL/assets/aglfn.txt").read_text().splitlines()
			for glyph_line in aglfn:
				glyph_cols = glyph_line.split(';')
				if self.name in glyph_cols:
					val = hex(int(glyph_cols[0], 16))
					self.rglyph.unicode = val



	def __get_width(self):
		w = 0
		for cell in self.cells[0]:
			w += cell.get_size()[0]
		return w


	def __carica_celle(self):

		# Reading CSV
		with open(self.path, "r") as csv_open:
			csv_reader = csv.reader(csv_open)
			gly_lines = [line for line in csv_reader]

		# Puntatore
		px = 0
		py = 0

		# Iterating over lines and saving cells
		for i, line in enumerate(reversed(gly_lines)):
			row = []
			for j, data in enumerate(line):
				cell = Cell(px, py, i=i, j=j, data=data.strip(), glyph=self)
				row.append(cell)
				w, h = cell.get_size()
				px += w
			self.cells.append(row)
			px = 0
			py += self.font.size[1]


	def render(self):
		for row in self.cells:
			for cell in row:
				cell.render()
		self.rglyph.removeOverlap()




class Cell:

	def __init__(self, px, py, i, j, data, glyph, thickness=10, negative=False):

		self.char   = data[0]
		self.rotate = int(data[1])
		self.extend = True if '*' in data else False

		self.i = i
		self.j = j

		self.glyph = glyph
		self.box = Box(px, py, *self.get_size())
		self.negative = negative



	def get_size(self):
		w, h = self.glyph.font.size
		if self.extend:
			pass
			w *= self.glyph.font.exp
		return (w, h)


	def render(self):

		# Interpolation factor
		f = self.j/(len(self.glyph.cells[0])-1)

		# # Climax Spessore
		# tck = interpolate_values(self.glyph.font.tck_min, self.glyph.font.tck, f)

		# # Anticlimax Spessore
		# tck = interpolate_values(self.glyph.font.tck, self.glyph.font.tck_min, f)



		sintassi[self.char](gly = self.glyph.rglyph,
							box = self.box,
							rot = self.rotate,
							tck = self.glyph.font.tck
							)