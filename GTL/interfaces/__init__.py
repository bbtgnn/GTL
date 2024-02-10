from typing import TypedDict, Mapping, List, Generic, TypeVar
from utils import Grid

#


class Glyph(TypedDict):
    name: str
    structure: str


Kind = TypeVar("Kind", str)
Parameters = TypeVar("Parameters", Mapping[str, str | int])


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
    upm: int
    em: int
    baseline: int
    cell_size: int
    x_height: int
    cap_height: int
    ascender: int


class Font(TypedDict):
    name: str
    syntax_list: List[Syntax]
    glyph_list: List[Glyph]
    metrics: Metrics
