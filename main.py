#imports
#import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
import pandas as pd

#sim setup:
t_end = 10.0
dt = 0.001
t0 = 0.0
n = int(np.ceil((t_end-t0)/dt))

#params: sigma, beta, rho
params = np.array([10.0,8/3, 28.0])

#initial cdtns: t, 
initialConditions= {'t':[t0],
                    'x':[0.001],
                    'y':[0.002],
                    'z':[0.003],
                    'x_dot':[0],
                    'y_dot':[0],
                    'z_dot':[0]}

#variables: x, y, z
df = pd.DataFrame(data=initialConditions)


def model(inputs, params):
    # inputs: series containing [ current x, current y, current z]
    # params: [sigma, beta, rho]
    # outputs: [current x_dot, current y_dot, current z_dot]
    x, y, z = inputs
    sigma, beta, rho = params
    current_x_dot = sigma * (y-x)
    current_y_dot = x * (rho - z) - y
    current_z_dot = x * y - beta * z

    outputs = {'x_dot':current_x_dot,
               'y_dot':current_y_dot,
               'z_dot':current_z_dot}
    return outputs

def integrateeuler(inputs, dt):
    #iputs: series containing [current x, current y, current z, current xdot, current ydot, current zdot] 
    #dt: dt 
    x, y, z, x_dot, y_dot, z_dot = inputs

    x_new = x + (x_dot*dt)
    y_new = y + (y_dot*dt)
    z_new = z + (z_dot*dt)
    outputs = {'x':x_new,
               'y':y_new,
               'z':z_new}
    return outputs


for timestep in range(n):
    #get previous values
    prev = df.iloc[timestep][['x', 'y', 'z']]
    #integrate
    newpos = integrateeuler(df.iloc[timestep][['x', 'y', 'z', 'x_dot', 'y_dot', 'z_dot']], 0.01)
    #add to df
    df = df.append(newpos, ignore_index=True) 
    #fill in time
    df['t'][(timestep+1)] = (timestep + 1)*dt
    #calc new derivs
    newderivs = model(df.iloc[timestep+1][['x', 'y', 'z']], params)
    df.loc[timestep+1, ['x_dot', 'y_dot', 'z_dot']] = [newderivs['x_dot'], newderivs['y_dot'], newderivs['z_dot']]
    
    print('{}/{}'.format(timestep, n))

df.to_csv('./data')
