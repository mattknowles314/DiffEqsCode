"""
T' = l - mu_T * T - k*T*V
I' = k*T*V - mu_I*I
V = N*mu_I*I - mu_V*V 

"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

def model(y, t, mu_I, mu_T, mu_V, l, k, N):
    T,I,V = y
    dTdt = l - mu_T*T - k*T*V
    dIdt = k*T*V - mu_I*I
    dVdt = N*mu_I*I - mu_V*V
    return dTdt, dIdt, dVdt

def makePlot():
    y0 = T0, I0, V0
    T,I,V = odeint(model, y0,t,args=(mu_I,mu_V,mu_T, l, k, N)).T

    plt.plot(t,T/1000, 'b', alpha=0.5, lw=2,label = 'Target')
    plt.plot(t,I/1000, 'r', alpha=0.5, lw=2,label = 'Infected') 
    plt.plot(t,V/1000, 'g', alpha=0.5, lw=2,label = 'Virions')
    plt.xlabel('Time')
    plt.ylabel('Proportion of Each Molecular Constituent in the Host')
    legend = plt.legend()
    plt.show()

t = np.linspace(start=1, stop=100, num=100)
T0 = 50
I0 = 0
V0 = 1
N = 10
mu_T = 2
mu_I = 5
mu_V = 3
k = 0.5
l = 10

makePlot()