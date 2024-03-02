# Automated Simulation Case Generation in OpenFOAM

This Bash script automates the generation and execution of multiple simulation cases in OpenFOAM. It allows for efficient parametric studies and sensitivity analyses in numerical simulations.

## Features

- Calculates coefficients and velocities based on given parameters.
- Creates a folder structure for each simulation case.
- Copies and adjusts configuration files and scripts for each case.
- Generates geometry and meshes it with Gmsh.
- Runs the simulation in parallel with mpirun.
- Performs post-processing operations with ParaView.
- Organizes results in the main folder structure.

## Usage

To use the script, simply execute it from the command line providing the number of cases as an argument. For example:

```bash
$ ./script.sh 5
