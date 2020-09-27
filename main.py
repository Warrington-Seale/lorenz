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

s= 10.0       # sigma          [-]
r= 28.0       # rho            [-]
b= 8/3        # beta           [-]
t0= 0.0       # initial time   [s]
tk= 10.0      # end time       [s]
dt= 0.001      # time step      [s]
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
    t, x, y, z = df.tail(1).T.values
    s, r, b, dt, tk = simParams
    
    if t >= tk:
        pass
    #euler for dx/dt, because it doesnt depend on t or x value
    k_x = dt * s * (y - z)
    x_new = x + k_x
    #R-K 4 for dy/dt
    k_y1 = dt * (x * (r - z) - y)
    k_y2 = dt *  (x * (r - z) - (y+0.5*k_y1))
    k_y3 = dt *  (x * (r - z) - (y+0.5*k_y2))
    k_y4 = dt *  (x * (r - z) - (y+k_y3))
    y_new = y + (1/6)*(k_y1 + 2*k_y2 + 2*k_y3 + k_y4)
    #R-K 4 for dz/dt
    k_z1 = dt * (x*y - b*z)
    k_z2 = dt * (x*y - b*(z+0.5*k_z1))
    k_z3 = dt * (x*y - b*(z+0.5*k_z2))
    k_z4 = dt * (x*y - b*(z+k_z3))
    z_new = z + (1/6)*(k_z1 + 2*k_z2 + 2*k_z3 + k_z4)
    #time
    t_new = t+dt
    #make array
    new = {'t': t_new, 'x': x_new, 'y': y_new, 'z':z_new,}
    #append it to the df
    return pd.DataFrame(data=new)

while 1:
    df = df.append(nextStep(df, simParams), ignore_index=True)
    print(df)
    input('next?')
