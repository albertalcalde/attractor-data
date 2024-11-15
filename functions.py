"""
Generate data from chaotic attractors in 3D ODEs from https://journals.aps.org/pre/pdf/10.1103/PhysRevE.50.R647
Added cases A, B, C.
"""

import numpy as np
from scipy.integrate import solve_ivp

def generate_traj_data(case, IC, T, dt):
    # Map the case number to the corresponding function
    cases = {
        'A': caseA,
        'B': caseB,
        'C': caseC
    }

    # Ensure the case is valid
    if case not in cases:
        raise ValueError(f"Invalid case: {case}. Choose from 'A', 'B' or 'C'.")

    # Retrieve the appropriate function
    case_function = cases[case]
    sol = solve_ivp(
        case_function, 
        [0, T], 
        IC, 
        method='RK45', 
        t_eval=np.linspace(0, T, int(T / dt))
    )
    data = sol.y
    np.save(f'case{case}.npy', data)
    return

def caseA(t, y): 
    return [y[1], -y[0] + y[1]*y[2], 1 - y[1]*y[1]]

def caseB(t, y): 
    return [y[1]*y[2], y[0] - y[1], 1 - y[0]*y[1]]

def caseC(t, y):
    return [y[1]*y[2], y[0] - y[1], 1 - y[0]*y[0]]


