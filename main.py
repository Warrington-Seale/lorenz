import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd



# Lorenz system equations:
# dx/dt = s(y-z)
# dy/dt = x(r-z)-y
# dz/dt = xy-bz
# s, r, b - parameters
# x, y, z - independent variables
# let's code runge-kutta 4th order by hand becacuse I can

s= 8.0        # sigma          [-]
r= 30.0       # rho            [-]
b= 2.59       # beta           [-]
t0= 0.0       # initial time   [s]
tk= 10.0      # end time       [s]
dt= 0.01      # time step      [s]
x0= 0.01      # initial x      [-]
y0= 0.02      # initial y      [-]
z0= 0.03      # initial z      [-]

simParams = [s, r, b, dt, tk]

initialConditions = {
        't': [t0], 
        'x': [x0],
        'y': [y0],
        'z': [z0],
        }

df = pd.DataFrame(data=initialConditions)

def nextStep(df, simParams):
    pass
