#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-


from __future__ import division, print_function, unicode_literals

from aiida.orm.code import Code
from aiida.orm import CalculationFactory
from aiida.work.launch import submit


def main():
    DifferenceCalculation = CalculationFactory('wait.wait')
    builder = DifferenceCalculation.get_builder()
    builder.code = Code.get_from_string('wait')
    builder.options = {
        'resources': {'num_machines': 1},
        'withmpi': False
    }

    node = submit(builder)
    print(node.pk)

if __name__ == '__main__':
    main()
