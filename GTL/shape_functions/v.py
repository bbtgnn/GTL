# -*- coding: utf-8 -*-
from ._utilities import *
from .diagonale import *


def v(gly, box, rot, tck):

	diagonale(gly, box, rot, tck)
	diagonale(gly, box, rot+1, tck)