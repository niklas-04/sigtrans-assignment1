import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#import sounddevice as sd

t0 = 0.01
f2 = 1000
deltaTime = 0.01
timeVector = np.arange(0, 10, deltaTime)

#Sine wave 1
amp1 = 1
phase1 = 0
omega1 = 2 * np.pi / t0

sine1 = amp1 * np.sin((omega1 + phase1))

#Sine wave 2
amp2 = 1
phase2 = 0
omega2 = 2 * np.pi * f2 
sine2 = amp2 * np.sin((omega2 + phase2))

y1 = np.zeros_like(timeVector)
y2 = np.zeros_like(timeVector)

for i in range(len(timeVector)):
    y1[i] = amp1 * np.sin((omega1 * timeVector[i] + phase1))
    y2[i] = amp2 * np.sin((omega2 * timeVector[i] + phase2))

fig, ax = plt.subplots()
ax.plot(timeVector, y1, label="Sine 1")
ax.plot(timeVector, y2, label="Sine 2")
plt.show()