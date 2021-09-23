import numpy as np

#sim setup:
config = {'t_end': 10,
        'dt': 0.001,
        't0': 0.0,
        'x0': 0.001,
        'y0': 0.001,
        'z0': 0.001,
        'x0_dot': 0,
        'y0_dot': 0,
        'z0_dot': 0,
        'sigma': 10.0,
        'beta': 8/3,
        'rho': 28.0,}



def runsim(config):
    n = int(np.ceil((config['t_end']-config['t0'])/config['dt'])) # no. of timesteps

    # preallocate the data matrix
    data = np.array([[0.0 for nvariables in range(3)] for timesteps in range(n)])
    # data[n][m]: n points to the timestep, m points to a variable in n-th timestep

    # apply positional initial conditions to the data matrix
    data[0] = [config['x0'], config['y0'], config['z0']]

    # prepare initial derivatives for the loop
    diffs = np.array([config['x0_dot'], config['y0_dot'], config['z0_dot']])

    for timestep in range(n-1):
        # calculate and save positions in next step
        data[timestep+1] = data[timestep] + np.multiply(diffs, config['dt'])

        #calculate diffs in new positionons
        x, y, z = data[timestep+1]
        x_dot = config['sigma'] * (y-x)
        y_dot = x * (config['rho'] - z) - y
        z_dot = x * y - config['beta'] * z
        #and make new diffs vector for next iteration
        diffs = np.array([x_dot, y_dot, z_dot])
        if timestep % 250 == 0: print('{} of {}'.format(timestep, n))
    return data

data = runsim(config)
