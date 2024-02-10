import itertools
from functools import reduce
from typing import List, TypeVar
from typing import Callable

A = TypeVar("A")


def flatten_list(l: List[List[A]]) -> List[A]:
    return list(itertools.chain.from_iterable(l))
