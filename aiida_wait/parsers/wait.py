#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiida.parsers.parser import Parser


class WaitParser(Parser):
    """
    Empty parser for the 'wait' calculation.
    """

    def parse_with_retrieved(self, retrieved):
        return True, []
