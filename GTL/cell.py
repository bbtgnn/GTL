from pathlib import Path
import fontParts.world as fp

from .. import GTL_syntax





class Typeface:

	def __init__(self, family_name, box, style_name="Regular"):
		self.family_name = family_name
		self.box = box
		self.glyphs = []
		self.rfont = fp.NewFont(family_name, style_name)


	def generate_glyphs(self, path):
		csv_list = Path(path).glob("**/*.csv")
		for csv_file in csv_list:
			self.glyphs.append(Glyph(self, csv_file))


	def render(self):
		for glyph in self.glyphs:
			glyph.render()


	def save_font(self, output_path):
		self.rfont.save(os.path.join(output_path, f'{self.family_name}.ufo'))



class Glyph:

	def __init__(self, font, path):
		self.font = font
		self.path = path
		self.name =	self.path.name[:-4]
		self.cells = []
		self.carica_celle()
		self.rglyph = self.font.rfont.newGlyph(self.name)
		self.rglyph.unicode = hex(ord(self.name))[2:].zfill(4)


	def carica_celle(self):
		with open(self.path, "r") as csv_open:
			csv_reader = csv.reader(csv_open)
			gly_lines = [line for line in csv_reader]

		# Puntatore
		px = 0
		py = 0

		for i, line in enumerate(gly_lines):
			for j, data in enumerate(line):

				x = j * self.font.box[0]
				y = i * self.font.box[1]
				w = self.font.box[0]*espansione
				h = self.font.box[1]

				cell_box = px, py, w, h
				self.cells.append(Cell(cell_box, s=data, glyph=self))

				px += w

			px = 0
			py += h


	def render(self):
		for cell in self.cells:
			cell.render()




class Cell:

	def __init__(self, box, data, glyph, thickness=10, espanso_oriz=1, espanso_vert=1):
		self.box = box
		self.char = data[0]
		self.modifier = data[1]
		self.glyph = glyph
		self.thickness = thickness


	def render(self, sintassi):
		sintassi[self.char](self.glyph, self.box)