""" 
File created by Albert Alcalde

Generate data for the 1D Wave equation by using d'Alembert's formula.
Last modified: 30-04-2025

"""

# %%
import numpy as np
from scipy.integrate import quad

def dAlembert_solution(x, t, c, f, g):
    """
    Evaluates d'Alembert solution to the 1D wave equation at point (x, t)
    
    Parameters:
    - x: float or np.array, spatial location(s)
    - t: float, time
    - c: float, wave speed
    - f: function, initial displacement u(x,0)
    - g: function, initial velocity ∂u/∂t(x,0)
    
    Returns:
    - u(x, t): value of the solution at (x, t)
    """
    x = np.asarray(x)
    u = 0.5 * (f(x - c*t) + f(x + c*t))
    
    def integral_term(xi):
        integral, _ = quad(g, xi - c*t, xi + c*t)
        return (1 / (2 * c)) * integral
    
    integral_vals = np.array([integral_term(xi) for xi in x])
    return u + integral_vals

# Initial conditions
# Define initial condition based on sum of sinuses
amplitudes = np.array((0.5, 1, 1.5))
wave_numbers = np.array((1,2,5))

def IC_SumOfSinus(X, amplitudes, wave_numbers):
    u0 = np.zeros_like(X)
    for A, k in zip(amplitudes, wave_numbers):
        u0 += A * np.sin(k * X)
    return u0


f = lambda x: IC_SumOfSinus(x, amplitudes, wave_numbers)# Displacement
g = lambda x: 0                  # Velocity

# Parameters
c = 1.0
L_x = 1.0
L_t = 10.0
N_x = 200
N_t = 1000
X = np.linspace(-L_x, L_x, N_x)
T = np.linspace(0, L_t, N_t + 1)

# Solution
U = np.array([dAlembert_solution(X, t, c, f, g) for t in T])

save = True
if save:
    np.save('waveEquation/1DwaveU.npy', U)
