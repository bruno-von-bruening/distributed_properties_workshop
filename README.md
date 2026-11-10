# Install
## Dummy environment
This is supposed to be merged with the super environment you will run in the workshop.
```bash
conda env create -f conda-env_alston_run_horton.yaml
```

You will have to install the run horton environment.

Currently, we also need run_psi4 and run_horton... (They can be installed in separate envo.)

I currently include mayavi there.



## Other envos needed
* run_psi4: only needs run_psi4
* run_horton: only needs horton but maybe more fragil

# Questions to Alston
* What's the backup?

# Problems
What if multipole runs of run scripts (will just create another file in same directory)

# TODOs

- [ ] Implement CI (problem is that I need other conda envs)
- [ ] Move all runs to work directory
