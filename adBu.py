'''
Two-Step Adam's Bashforth Method


y_(n+1) = y_n + 3/2*h*f(t_n,y_n) - 1/2*h*f(t_(n-1),y_(n-1))

'''

import numpy as np 
import matplotlib.pyplot as plt

'''
    ode_solve: Performs Adams' Bashforth method on a given function f

    f (callable): first order ODE to be solved
    y0 (array): initial condition
    t (array): a sequence of time points to solve the ODE at
    args (dict): extra arguments that get passed
'''
def ode_solve(f, y0, t, args={}):
    
    #We first initialise an approximation array
    y = np.zeros([len(t), len(y0)])
    y[0] = y0

    #Implementing the formula
    for i, t_i in enumerate(t[2:-1], start=2):
        h = t[i+1] - t_i
        y[i+1] = y[i] + (1.5*h*f(t_i, y[i], args) - 0.5*h*f(t[i-1], y[i-1], args))

    return y
