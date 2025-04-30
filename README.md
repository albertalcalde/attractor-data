# Chaotic Attractors in 3D ODEs

This repository contains code for generating data from chaotic attractors in 3D ordinary differential equations (ODEs) based on the models presented in [Phys. Rev. E 50, R647 (1994)](https://journals.aps.org/pre/pdf/10.1103/PhysRevE.50.R647). The code includes cases (A, B, C) for experimentation and analysis.

## Features

- Generates time series data from chaotic attractors in 3D ODEs.
- Option to customize the initial condition (IC), integration time (T), step size (dt) of the ODE solver.

## Wave equation in 1D
This repository also contains code for solving the 1D wave equation using d'Alembert's formula. If the spatial domain is discretized in N_x points and the data is sampled at N_t + 1 timesteps, the time series data constists of N_t + 1 snapshots of dimension N_x containing the solution of the wave equation.