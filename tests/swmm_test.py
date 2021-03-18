import os
import unittest

from swmm5.basic_api import run_swmm


class SWMMTest(unittest.TestCase):
    def test_if_run_swmm_stdout_status_0(self):
        # Model ParallelPumpConfiguration.inp was downloaded from
        # https://www.openswmm.org/Topic/16763/parallel-pump-configuration
        res = run_swmm("resources/ParallelPumpConfiguration.inp")

        assert res.returncode == 0

        # cleaning
        os.remove("ParallelPumpConfiguration.rpt")
        os.remove("ParallelPumpConfiguration.out")
