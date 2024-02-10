import GTL.interfaces as GTL
import fontParts.base as FP
import fontParts.world as fp
from GTL.interfaces.utils import FPMetrics
from typing import List, cast
from functools import reduce, partial
from draw import draw_glyph


#


def create_font(family_name: str, style_name: str) -> FP.BaseFont:
    return cast(FP.BaseFont, fp.NewFont(family_name, style_name, False))

#


def calc_font_metrics(metrics: GTL.Metrics) -> FPMetrics:
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
    font_clone = font.copy()
    font_clone.info = calc_font_metrics(metrics)
    return font_clone

#


def add_glyph_to_font(font: FP.BaseFont, glyph: FP.BaseGlyph) -> FP.BaseFont:
    font_clone = font.copy()
    font_clone[glyph.name] = glyph
    return font_clone


def draw_glyph_in_font(font: FP.BaseFont, glyph: GTL.Glyph, metrics: GTL.Metrics, syntax: GTL.Syntax) -> FP.BaseFont:
    return add_glyph_to_font(font, draw_glyph(glyph, metrics, syntax))


def draw_glyph_list_in_font(font: FP.BaseFont, glyph_list: List[GTL.Glyph], metrics: GTL.Metrics, syntax: GTL.Syntax) -> FP.BaseFont:
    return reduce(
        partial(
            draw_glyph_in_font,
            metrics=metrics,
            syntax=syntax
        ),
        glyph_list,
        font
    )

#


def draw_font(glyph_list: List[GTL.Glyph], metrics: GTL.Metrics, syntax: GTL.Syntax, font_name: str) -> FP.BaseFont:
    font = create_font(font_name, syntax['name'])
    font = set_font_metrics(font, metrics)
    font = draw_glyph_list_in_font(font, glyph_list, metrics, syntax)
    return font
