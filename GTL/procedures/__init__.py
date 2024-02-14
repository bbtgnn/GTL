import GTL.interfaces as GTL
import fontParts.base as FP
import fontParts.world as fp
from GTL.interfaces.utils import FPMetrics
from typing import List, cast
from draw import draw_glyph

# - Main - #


def draw_font_family(font: GTL.Font) -> List[FP.BaseFont]:
    return [draw_font_style(font['glyph_list'], font['metrics'], syntax, font['name']) for syntax in font['syntax_list']]


def draw_font_style(glyph_list: List[GTL.Glyph], metrics: GTL.Metrics, syntax: GTL.Syntax, font_name: str) -> FP.BaseFont:
    font = create_fp_font(font_name, syntax['name'])
    font = set_font_metrics(font, metrics)
    font = draw_glyph_list_in_font(font, glyph_list, metrics, syntax)
    return font

# - Create font - #


def create_fp_font(family_name: str, style_name: str) -> FP.BaseFont:
    return cast(FP.BaseFont, fp.NewFont(family_name, style_name, False))

# - Metrics management - #


def calc_fp_font_metrics(metrics: GTL.Metrics) -> FPMetrics:
    cell_size = metrics['cell_size']
    info = {
        "unitsPerEm": cell_size * metrics['em'],
        "descender": - cell_size * metrics['baseline'],
        "xHeight": cell_size * metrics['x_height'],
        "capHeight": cell_size * metrics['cap_height'],
        "ascender": cell_size * metrics['ascender']
    }
    return cast(FPMetrics, info)


def set_font_metrics(font: FP.BaseFont, metrics: GTL.Metrics) -> FP.BaseFont:
    font.info = calc_fp_font_metrics(metrics)
    return font

# - Adding glyphs - #


def draw_glyph_list_in_font(font: FP.BaseFont, glyph_list: List[GTL.Glyph], metrics: GTL.Metrics, syntax: GTL.Syntax) -> FP.BaseFont:
    for glyph in glyph_list:
        draw_glyph_in_font(font, glyph, metrics, syntax)
    return font


def draw_glyph_in_font(font: FP.BaseFont, glyph: GTL.Glyph, metrics: GTL.Metrics, syntax: GTL.Syntax) -> FP.BaseFont:
    return add_glyph_to_font(font, draw_glyph(glyph, metrics, syntax))


def add_glyph_to_font(font: FP.BaseFont, glyph: FP.BaseGlyph) -> FP.BaseFont:
    font[glyph.name] = glyph
    return font
