#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>

from __future__ import division, print_function, unicode_literals

from aiida.orm.code import Code
from aiida.orm import DataFactory, CalculationFactory
from aiida.work.run import run


def main():
    DifferenceCalculation = CalculationFactory('wait.difference')
    process = DifferenceCalculation.process()
    inputs = process.get_inputs_template()
    inputs.code = Code.get_from_string('wait_dev')
    inputs._options.resources = {'num_machines': 1}
    inputs._options.withmpi = False

    BandsData = DataFactory('array.bands')
    bands1 = BandsData()
    bands2 = BandsData()
    kpoints = [[0.1, 0.2, 0.3], [0., 0.5, 0.5]]
    bands1.set_kpoints(kpoints)
    bands2.set_kpoints(kpoints)
    bands1.set_bands([[1, 2, 3], [1, 2, 3]])
    bands2.set_bands([[2, 2, 3], [1, 2, 2]])

    inputs.bands1 = bands1
    inputs.bands2 = bands2

    output = run(process, **inputs)
    print('Difference:', output['output_parameters'].dict['diff'])


if __name__ == '__main__':
    main()