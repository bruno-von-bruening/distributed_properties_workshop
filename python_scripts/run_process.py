
from contextlib import chdir 
import subprocess as sp, os
from qcp_global_utils.shell_processes.execution import run_shell_command

def run_subrocess(cmd, directory=None):
    if directory is None: directory=os.getcwd() # If no directory provided run in pwd (present working directory)
    elif not os.path.isdir(directory): os.mkdir(directory)

    # Could also delete if necessary
    with chdir(directory):
        # print(f"Running horton in  {the_dir}")
        run_shell_command(cmd)
        # proc=sp.run(cmd.split(), capture_output=True)
