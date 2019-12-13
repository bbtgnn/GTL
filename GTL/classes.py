### MODULES

import os
import csv

from pathlib import Path
import fontParts.world as fp

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

	def __init__(self, family_name, wh, style_name="Regular", espansione=1):
		self.family_name = family_name
		self.wh = wh
		self.glyphs = []
		self.espansione = espansione
		self.rfont = fp.NewFont(family_name, style_name)


	def generate_glyphs(self, path):
		csv_list = Path(path).glob("**/*.csv")
		for csv_file in csv_list:
			gly = Glyph(self, csv_file)
			self.glyphs.append(gly)


	def render(self):
		for glyph in self.glyphs:
			glyph.render()


	def save_font(self, output_path):
		self.rfont.save(os.path.join(output_path, f'{self.family_name}.ufo'))



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
		self.rglyph.unicode = self.__unicode_name()


	def __unicode_name(self):
		if "." in self.name:
			return None
		return hex(ord(self.name))[2:].zfill(4)


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
				cell = Cell(px, py, i=i, j=j, data=data, glyph=self)
				row.append(cell)
				w, h = cell.get_size()
				px += w
			self.cells.append(row)
			px = 0
			py += self.font.wh[1]


	def render(self):
		for row in self.cells:
			for cell in row:
				cell.render()




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
		w, h = self.glyph.font.wh
		if self.extend:
			w *= lunghezza_espansione
		return (w, h)


	def render(self):
		sintassi[self.char](gly = self.glyph.rglyph,
							box = self.box,
							rot = self.rotate,
							tck = tck
							)

		# for row in self.glyph.cells:
		# if self.negative:
		# 	pen = self.glyph.rglyph.getPen()
		# 	############
		# 	## MAKE CLOCKWISE RECTANGLE
		# 	x, y, w, h = self.box
		# 	pen.moveTo((x  -w/2,y))
		# 	pen.lineTo((x  -w/2, y+h))
		# 	pen.lineTo((x+w-w/2, y+h))
		# 	pen.lineTo((x+w-w/2, y))
		# 	pen.closePath()