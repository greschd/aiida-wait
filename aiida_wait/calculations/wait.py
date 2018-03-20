# -*- coding: utf-8 -*-

from aiida.orm import JobCalculation, DataFactory
# from aiida.common.utils import classproperty
from aiida.common.datastructures import CalcInfo, CodeInfo


class WaitCalculation(JobCalculation):
    def _init_internal_params(self):
        super(DifferenceCalculation, self)._init_internal_params()

        self._OUTPUT_FILE_NAME = 'diff.txt'
        self._default_parser = 'wait.wait'

    def _prepare_for_submission(self, tempfolder, inputdict):
        calcinfo = CalcInfo()
        calcinfo.uuid = self.uuid
        calcinfo.remote_copy_list = []
        calcinfo.retrieve_list = []

        codeinfo = CodeInfo()
        codeinfo.cmdline_params = []
        codeinfo.stdout_name = self._OUTPUT_FILE_NAME
        codeinfo.code_uuid = code.uuid
        calcinfo.codes_info = [codeinfo]

        return calcinfo
