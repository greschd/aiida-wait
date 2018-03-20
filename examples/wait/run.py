#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from aiida.orm import DataFactory, CalculationFactory


def run():
    code = Code.get_from_string('wait')
    calc = CalculationFactory('wait.wait')()
    calc.use_code(code)

    calc.set_resources(dict(num_machines=1, tot_num_mpiprocs=1))
    calc.set_withmpi(False)
    calc.set_computer(Computer.get('localhost'))
    calc.store_all()
    calc.submit()
    print('Submitted calculation', calc.pk)


if __name__ == '__main__':
    run()
