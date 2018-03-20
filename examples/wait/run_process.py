#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-


from __future__ import division, print_function, unicode_literals

from aiida.orm.code import Code
from aiida.orm import CalculationFactory
from aiida.work.run import run


def main():
    DifferenceCalculation = CalculationFactory('wait.wait')
    process = DifferenceCalculation.process()
    inputs = process.get_inputs_template()
    inputs.code = Code.get_from_string('wait')
    inputs._options.resources = {'num_machines': 1}
    inputs._options.withmpi = False

    output = run(process, **inputs)
    print('Difference:', output['output_parameters'].dict['diff'])

if __name__ == '__main__':
    main()
