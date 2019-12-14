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
		self.line_num = self.config["line_num"]
		self.cell_hgt = base * round(self.UPM / self.line_num / base)
		self.cell_wdt = self.cell_hgt * self.config["size_ratio"]
		self.size = self.cell_wdt, self.cell_hgt

		self.tck = self.config["tck"]
		self.tck_min = self.config["tck_min"]
		self.sqr = self.config["sqr"]
		self.inv = self.config["inv"]
		self.allungamento = self.config["allungamento"]

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
		# self.rglyph.removeOverlap()




class Cell:

	def __init__(self, px, py, i, j, data, glyph, thickness=10):

		self.char   = data[0]
		self.rotate = int(data[1])
		self.extend = True if '*' in data else False

		self.i = i
		self.j = j

		self.glyph = glyph
		self.box = Box(px, py, *self.get_size())



	def get_size(self):
		w, h = self.glyph.font.size
		if self.extend:
			w *= self.glyph.font.allungamento
		return (w, h)


	def render(self):

		# # Climax verticale
		# vf = self.i/self.glyph.font.line_num

		# # Climax orizzontale
		# hf = self.j/len(self.glyph.cells[0])

		# # Climax
		# tck = interpolate_values(self.glyph.font.tck, self.glyph.font.tck_min, hf)

		# # Interpolation factor
		# f = self.i/(len(self.glyph.cells[0]))

		# # Climax Spessore
		# tck = interpolate_values(self.glyph.font.tck_min, self.glyph.font.tck, f)

		# Anticlimax Spessore

		if self.extend and self.glyph.font.allungamento == 0:
			return


		sintassi[self.char](gly = self.glyph.rglyph,
							box = self.box,
							rot = self.rotate,
							tck = self.glyph.font.tck
							)