
from contextlib import chdir 
from conda_env import get_python_from_conda_env
import subprocess as sp, os
import numpy as np
from typing import Literal

def run_horton_inner(python_path, horton_script, fchk_file:str, method='LISA'):
    the_dir=f"horton_run"
    if not os.path.isdir(the_dir): os.mkdir(the_dir)
    with chdir(the_dir):
        # print(f"Running horton in  {the_dir}")
        cmd=f"{python_path} {horton_script} --exc --wfn {fchk_file} --method {method}"
        proc=sp.run(cmd.split(), capture_output=True)

def run_horton(fchk_file:str, python_path:str|None=None, method:Literal['MBIS','LISA']='LISA'):
    """ Currently does not take argument 
    Be aware that there a different methods (e.g. LISA and MBIS)
    """
    
    # The file needs to exist!
    assert os.path.isfile(fchk_file), f"Not an existing file: \"{fchk_file}\""
    fchk_file=os.path.realpath(fchk_file)

    # A environment needs to exist
    if python_path is None:
        try:
            python_path = get_python_from_conda_env('run_horton')
        except Exception as e:
            raise RuntimeError("Could not find the horton script. Please provide the path to the script or ensure that the conda environment 'run_horton' is available.") from e
    else:
        assert os.path.isfile(python_path), f"Provided python path does not exist: \"{python_path}\""

    #
    horton_script=python_path.replace('python','run_horton_wpart.py')


    # Could Test that horton_scrip works
    run_horton_inner(python_path, horton_script, fchk_file, method=method)

def load_horton_moments(the_dir):
    """ Loads the moments from LISA_moments.txt file """
    if not os.path.isdir(the_dir):
        raise NotADirectoryError(f"Provided directory does not exist: {the_dir}")
    with chdir(the_dir):
        expected_moments_file='LISA_moments.txt'
        if not os.path.isfile(expected_moments_file):
            raise FileNotFoundError(f"Expected moments file not found: {expected_moments_file}")
        
        # Get this into array.
        with open(expected_moments_file, 'r') as rd:
            try: 
                moments=np.array([ [float(x) for x in line.split()] 
                            for line in rd.readlines() ])
            except Exception as ex:
                raise ValueError(f"Error reading moments from {expected_moments_file}: {ex}")
        
    return moments