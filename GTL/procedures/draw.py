import GTL.interfaces as GTL
from GTL.interfaces.utils import Cell
import fontParts.base as FP
from fontTools.pens.basePen import BasePen
from typing import cast, List
from utils import flatten_list
from functools import reduce
from unicode import set_glyph_unicode

# - #


def set_glyph_name(glyph: FP.BaseGlyph, name: str) -> FP.BaseGlyph:
    glyph.name = name
    return glyph

# - #


def calc_cells_from_structure(structure: GTL.GlyphStructure, metrics: GTL.Metrics, cell_width: float) -> List[Cell]:
    cells: List[Cell] = []

    cell_height = metrics['cell_size']
    cell_width = round(cell_height * cell_width)
    cell_x = 0
    cell_y = - cell_height * metrics['baseline']

    # TODO – Remove loops
    for row in structure[::-1]:
        for symbol in row:
            cells.append({
                'x': cell_x,
                'y': cell_y,
                'w': cell_width,
                'h': cell_height,
                'symbol': symbol
            })
            cell_x += cell_width
        cell_x = 0
        cell_y += cell_height

    return cells

#


def get_glyph_pen(glyph: FP.BaseGlyph) -> BasePen:
    return cast(BasePen, glyph.getPen())


def draw_cell_content(cell: Cell, syntax: GTL.Syntax) -> List[FP.BaseContour]:
    return []

#


def add_contour_to_glyph(glyph: FP.BaseGlyph, contour: FP.BaseContour) -> FP.BaseGlyph:
    glyph_clone = glyph.copy()
    glyph_clone.appendContour(contour)
    return glyph_clone


def add_contour_list_to_glyph(glyph: FP.BaseGlyph, contour_list: List[FP.BaseContour]) -> FP.BaseGlyph:
    return reduce(
        add_contour_to_glyph,
        contour_list,
        glyph
    )

#


def set_glyph_contours(glyph: FP.BaseGlyph, structure: GTL.GlyphStructure, metrics: GTL.Metrics, syntax: GTL.Syntax) -> FP.BaseGlyph:
    cell_list = calc_cells_from_structure(
        structure, metrics, syntax['width'])
    contour_list = flatten_list([draw_cell_content(cell, syntax)
                                 for cell in cell_list])
    glyph = add_contour_list_to_glyph(glyph, contour_list)
    return glyph


# - #


def draw_glyph(glyph: GTL.Glyph, metrics: GTL.Metrics, syntax: GTL.Syntax) -> FP.BaseGlyph:
    fp_glyph = FP.BaseGlyph()
    fp_glyph = set_glyph_name(fp_glyph, glyph['name'])
    fp_glyph = set_glyph_unicode(fp_glyph)
    fp_glyph = set_glyph_contours(
        fp_glyph, glyph['structure'], metrics, syntax)
    return fp_glyph
