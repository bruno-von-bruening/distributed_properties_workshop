# distributed_properties_workshop
Might change the name

For Alston: provide some description and relevant citations here

## Install

## Main environment (which runs notebooks)
This is supposed to be merged with the super environment you will run in the workshop.
```bash
conda env create -f conda-env_alston_run_horton.yaml
```

Within the jupyter notebooks then choose this enviornment as ipykernel! 

This environment will include a custom molecule viewer using the mayavi package (https://github.com/enthought/mayavi):
https://github.com/bruno-von-bruening/mayavi_molecule_viewer
This custom package will be called in the notebooks to visualize electrostatic potentials!

## Dependent environments
You will have to install three other environment that live independently on your system (each an independent conda install):
* run_psi4: generates and runs input files with psi4 [^1]:
https://github.com/bruno-von-bruening/run_psi4
* run_horton: generates and runs input files wrapping around horton-wpart project [^2]:
https://github.com/bruno-von-bruening/run_horton
* qcp_dens: custom code computing iso-densit surfaces and evaluating electrostatis. This used `qc-grid`[^3] and `qc-basis`[^4] projects:
https://github.com/bruno-von-bruening/qcp_density_operations

** THE NOTEBOOKS WILL NOT WORK WITHOUT INSTALLING THESE ADDITIONAL CONDA ENVIRONMENTS **

For the corresponding installation please visit these links; all follow a simple conda environment creation for the installation of dependencies and subsequent pip installation of the local package.

The reason for handling these packages separately is clash between dependency requirements (esp the run_horton and mayavi dependencies are rather inflexible). 

# Questions to Alston
* What's the backup?



## References
[^1]: Smith, D. G. A.; Burns, L. A.; Simmonett, A. C.; Parrish, R. M.; Schieber, M. C.; Galvelis, R.; Kraus, P.; Kruse, H.; Di Remigio, R.; Alenaizan, A.; James, A. M.; Lehtola, S.; Misiewicz, J. P.; Scheurer, M.; Shaw, R. A.; Schriber, J. B.; Xie, Y.; Glick, Z. L.; Sirianni, D. A.; O’Brien, J. S.; Waldrop, J. M.; Kumar, A.; Hohenstein, E. G.; Pritchard, B. P.; Brooks, B. R.; Schaefer, H. F.; Sokolov, A. Yu.; Patkowski, K.; DePrince, A. E.; Bozkaya, U.; King, R. A.; Evangelista, F. A.; Turney, J. M.; Crawford, T. D.; Sherrill, C. D. P SI4 1.4: Open-source software for high-throughput quantum chemistry. *The Journal of Chemical Physics* **2020**, 152 (18), 184108. https://doi.org/10.1063/5.0006002.
see github project: https://github.com/psi4/psi4/

[^2]: Cheng, Y.; Cancès, E.; Ehrlacher, V.; Misquitta, A. J.; Stamm, B. Multi-center decomposition of molecular densities: A numerical perspective. *The Journal of Chemical Physics* **2025**, 162 (7). https://doi.org/10.1063/5.0245287.
see github project: https://github.com/LISA-partitioning-method/horton-part


[^3]: Tehrani, A.; Yang, X. D.; Martínez-González, M.; Pujal, L.; Hernández-Esparza, R.; Chan, M.; Vöhringer-Martinez, E.; Verstraelen, T.; Ayers, P. W.; Heidar-Zadeh, F. Grid: A Python library for molecular integration, interpolation, differentiation, and more. *The Journal of Chemical Physics* **2024**, 160 (17). https://doi.org/10.1063/5.0202240.
See github project: https://github.com/theochem/grid/

[^4]: Kim, T. D.; Pujal, L.; Richer, M.; Van Zyl, M.; Martínez-González, M.; Tehrani, A.; Chuiko, V.; Sánchez-Díaz, G.; Sanchez, W.; Adams, W.; Huang, X.; Kelly, B. D.; Vöhringer-Martinez, E.; Verstraelen, T.; Heidar-Zadeh, F.; Ayers, P. W. GBasis: A Python library for evaluating functions, functionals, and integrals expressed with Gaussian basis functions. *The Journal of Chemical Physics* **2024**, 161 (4). https://doi.org/10.1063/5.0216776.
See github project: https://github.com/theochem/gbasis
