import os
import subprocess
from sys import platform as _platform

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _get_swmm_path():
    # UNIX
    swmm_path = os.path.join(ROOT_DIR, 'lib', 'linux', 'swmm5')

    # WINDOWS
    if _platform.startswith("win"):
        swmm_path = os.path.join(ROOT_DIR, 'lib', 'windows', 'swmm5.exe')
    return swmm_path


def run_swmm(input_file):
    swmm_path = _get_swmm_path()
    input_file_name = os.path.basename(input_file).split(".")[0]
    return subprocess.run(
        swmm_path + " " + input_file + " " + input_file_name + ".rpt" + " " + input_file_name + ".out",
        shell=True,
        check=True)
