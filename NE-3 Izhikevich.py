import numpy as np
import matplotlib.pyplot as plt

x  = 5
y  = 140

titles = ['thalamo-cortical #2']
a  = [0.02]
b  = [0.25]
c  = [-65]
d  = [0.05]

v0 = -87  # Resting potential        [mV]
T = 200  # Simulation time          [mSec]
dt = 0.25  # Simulation time interval [mSec]

time = np.arange(0, T + dt, dt)  # Time array

stim = np.zeros(len(time))
for i, t in enumerate(stim):
    if 0 <= i <= 50:
        stim[i] = -25
    if 50 < i:
        stim[i] = 0

trace = np.zeros((2, len(time)))  # Tracing du and dv

for exp in range(len(a)):
    v = v0
    u = b[exp] * v
    spikes = []
    for i, j in enumerate(stim):
        v += dt * (0.04 * v ** 2 + x * v + y - u + stim[i])
        u += dt * a[exp] * (b[exp] * v - u)
        if v > 30:
            trace[0, i] = 30
            v = c[exp]
            u += d[exp]
        else:
            trace[0, i] = v
            trace[1, i] = u

    plt.figure(figsize=(10, 5))
    plt.title('Izhikevich Model: {}'.format(titles[exp]), fontsize=15)
    plt.ylabel('Membrane Potential (mV)', fontsize=15)
    plt.xlabel('Time (msec)', fontsize=15)
    plt.plot(time, trace[0], linewidth=2, label='Vm')
    plt.plot(time, trace[1], linewidth=2, label='Recovery', color='green')
    plt.plot(time, stim + v0, label='Stimuli (Scaled)', color='sandybrown', linewidth=2)
    plt.legend(loc=1)
    plt.show()