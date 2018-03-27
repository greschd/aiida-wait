#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from aiida.orm import DataFactory, CalculationFactory


def run():
    code = Code.get_from_string('wait_remote')
    calc = CalculationFactory('wait.wait')()
    calc.use_code(code)

    calc.set_resources(dict(num_machines=1, tot_num_mpiprocs=1))
    calc.set_withmpi(False)
    calc.set_computer(Computer.get('monch'))
    calc.set_queue_name('dphys_compute')
    calc.set_resources({'num_machines': 1})
    calc.store_all()
    calc.submit()
    print('Submitted calculation', calc.pk)


if __name__ == '__main__':
    run()
