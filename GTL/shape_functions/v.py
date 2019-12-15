# -*- coding: utf-8 -*-
from ._utilities import *
from .diagonale import *


def v(gly, box, rot, tck, *arg):

	d = {
		0: [2, 1],
		1: [0, 1],
		2: [3, 0],
		3: [3, 2]
	}

	diagonale(gly, box, d[rot][0], tck)
	diagonale(gly, box, d[rot][1], tck)