from typing import TypedDict


class Grid(TypedDict):
    rows: int
    columns: int


class Cell(TypedDict):
    x: int
    y: int
    w: int
    h: int
    symbol: str


class FPMetrics(TypedDict):
    unitsPerEm: int
    descender: int
    xHeight: int
    capHeight: int
    ascender: int
