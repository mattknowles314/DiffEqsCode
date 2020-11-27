'''
Two-Step Adam's Bashforth Method

- https://ogden.eu/the-two-step-adams-bashforth-method-with-different-stepsizes -

y_(n+1) = y_n + 3/2*h*f(t_n,y_n) - 1/2*h*f(t_(n-1),t_(n-1))

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
    y = np.zeros([len(t), len(y0)])
    y[0] = y0

