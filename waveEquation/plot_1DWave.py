import numpy as np
import matplotlib.pyplot as plt
from scipy import meshgrid

load = True
if load:
    U = np.load('waveEquation/1DwaveU.npy')

# Parameters
c = 1.0
L_x = 1.0
L_t = 10
N_x = 200
N_t = 1000
X = np.linspace(-L_x, L_x, N_x)
T = np.linspace(0, L_t, N_t + 1)

def plot_spatio_temp(x,y,t):
    V = y[::-1, :]
    plt.figure(figsize=(6,5))
    plt.imshow(V, extent=[0,x[y.shape[1] - 1],0,t[y.shape[0] - 1]])


    cbar = plt.colorbar()
    cbar.set_label('height $[m]$')
    plt.xlabel('$x \ [\mathrm{m}]$')
    plt.ylabel('$t \ [\mathrm{s}]$')
    plt.axis('auto')
    # plt.show()

plot_spatio_temp(X,U,T)
plt.savefig('waveEquation/1Dwave_spatio_temp.pdf')