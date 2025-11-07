import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#import sounddevice as sd

#Helper func for use in several tasks
def sines(timeVector):
    t1 = 0.01
    f2 = 1000
    #Sine wave 1 (x1)
    amp1 = 1
    phase1 = 0
    omega1 = 2 * np.pi / t1

    # x1 = amp1 * np.sin((omega1 + phase1))

    #Sine wave 2 (x2)
    amp2 = 1
    phase2 = 0
    omega2 = 2 * np.pi * f2 
    # x2 = amp2 * np.sin((omega2 + phase2))

    x1 = np.zeros_like(timeVector)
    x2 = np.zeros_like(timeVector)

    for i in range(len(timeVector)):
        x1[i] = amp1 * np.sin((omega1 * timeVector[i] + phase1))
        x2[i] = amp2 * np.sin((omega2 * timeVector[i] + phase2))

    return x1, x2


# Task 1
def task1():
    deltaTime = 0.01 * 10**-3
    timeVector = np.arange(0, 5, deltaTime)

    
    x1, x2 = sines(timeVector)

    #sd.play(y1, 1/dt, blocking=True)

    fig, ax = plt.subplots()
    ax.plot(timeVector, x1, label="x1(t)")
    ax.plot(timeVector, x2, label="x2(t)")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("x(t)")

    ax.legend()

    ax.set_xlim(0, 10 * 10**-3)
    ax.set_ylim(-1.1, 1.1)

    plt.show()

#Task 2
def task2():
    alpha = 1000 * np.pi
    deltaTime = 0.01 * 10**-3
    timeVector = np.arange(0, 20 * 10**-3, deltaTime)
    
    diracDelta = np.zeros_like(timeVector)
    diracDelta[0] = 1 / deltaTime

    h = np.zeros_like(timeVector)
    for i in range(len(timeVector)):
        h[i] = alpha**2 * timeVector[i] * np.exp(-alpha * timeVector[i])


    y = deltaTime * signal.convolve(diracDelta, h, method = 'direct')
    y = y[0: diracDelta.shape[0]]


    fig, ax = plt.subplots()
    ax.plot(timeVector, h, label="impulse response (h)")
    ax.plot(timeVector, y, label="dirac delta * h (convolution)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("y(t)")
    ax.set_xlim(0, 5 * 10**-3)
    ax.legend()
    plt.show()

#Task 3
def task3():
    alpha = 1000 * np.pi
    deltaTime = 0.01 * 10**-3
    timeVector = np.arange(0, 20 * 10**-3, deltaTime)

    x1, x2 = sines(timeVector)
    
    h = np.zeros_like(timeVector)
    for i in range(len(timeVector)):
        h[i] = alpha**2 * timeVector[i] * np.exp(-alpha * timeVector[i])

    y1 = deltaTime * signal.convolve(x1, h, method = 'direct')
    y1 = y1[0: x1.shape[0]]

    y2 = deltaTime * signal.convolve(x2, h, method = 'direct')
    y2 = y2[0: x2.shape[0]]

    fig, ax = plt.subplots()
    ax.plot(timeVector, y1, label="y1(t)")
    ax.plot(timeVector, y2, label="y2(t)")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("y(t)")
    ax.legend()
    ax.set_xlim(0, 20 * 10**-3)
    ax.set_ylim(-1, 1)
    plt.show()

#Task 4
def task4():
    def sumArr(in1, in2):
        out = np.zeros_like(in1)
        for i in range(len(in1)):
            out[i] = in1[i] + in2[i]
        return out
    
    alpha = 1000 * np.pi
    deltaTime = 0.01 * 10**-3
    timeVector = np.arange(0, 20 * 10**-3, deltaTime)
    
    x1, x2 = sines(timeVector)

    x3 = sumArr(x1, x2)

    h = np.zeros_like(timeVector)
    for i in range(len(timeVector)):
        h[i] = alpha**2 * timeVector[i] * np.exp(-alpha * timeVector[i])

    y1 = deltaTime * signal.convolve(x1, h, method = 'direct')
    y1 = y1[0: x1.shape[0]]

    y2 = deltaTime * signal.convolve(x2, h, method = 'direct')
    y2 = y2[0: x2.shape[0]]

    y12 = sumArr(y1, y2)

    y3 = deltaTime * signal.convolve(x3, h, method = 'direct')
    y3 = y3[0: x3.shape[0]]

    fig, ax = plt.subplots()
    ax.plot(timeVector, y3, label="y3(t)")
    ax.plot(timeVector, y12, label="y1(t) + y2(t)")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("y(t)")
    ax.legend()
    ax.set_xlim(0, 20 * 10**-3)
    plt.show()

#To run, uncomment the desired task
#task1()
#task2()
task3()
#task4()