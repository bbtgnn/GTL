from typing import TypedDict, Mapping, List, Generic, TypeVar
from utils import Grid

#

type GlyphStructure = List[List[str]]


class Glyph(TypedDict):
    name: str
    structure: GlyphStructure


Kind = TypeVar("Kind", bound=str)
Parameters = TypeVar(
    "Parameters", bound=Mapping[str, str | int | float])


class ShapeInstructions(TypedDict, Generic[Kind, Parameters]):
    kind: Kind
    parameters: Parameters


class Rule(TypedDict):
    symbol: str
    instructions: ShapeInstructions


class Syntax(TypedDict):
    name: str
    rules: List[Rule]
    layout: Grid
    width: float
    # TODO - add slant: float (angle)


class Metrics(TypedDict):
    cell_size: int
    em: int
    baseline: int
    x_height: int
    cap_height: int
    ascender: int


class Font(TypedDict):
    name: str
    syntax_list: List[Syntax]
    glyph_list: List[Glyph]
    metrics: Metrics
