# m = mass in kg
# g = acceleration due to gravity in m/s^2
# h0 = initial height in m
# vel0 = initial velocity in m/s
# accel0 = initial acceleration in m/s^2 (before thrust becomes 0)
# hs = an array holding instantaneous heights in m
# vels = an array holding instantaneous velocities in m/s
# accels = an array holding instantaneous accelerations in m/s^2
# ts = an array of time in s
# velFinalWithThrust = final velocity when thrust is present in m/s
# deltaYAscendWithThrust = change in heights when thrust is present in m
# deltaY = change in total height in m
# velFinalWithoutThrust = final velocity when the rocket reaches the ground in m/s
# timeWithoutThrustDescend = time when the rocket is descending in s
# timeWithoutThrust = total time without thurst in s
# totalTime = total time for the whole trajectory in s

import matplotlib.pyplot as plt
import numpy as np

m = 1
g = -10
timeWithThrust = 3

h0 = 0
vel0 = 0
accel0 = 5

hs = []
vels = []
accels = []
time = []

hs.append(h0)
vels.append(vel0)
accels.append(accel0)
time.append(0)

velFinalWithThrust = timeWithThrust * accel0
deltaYAscendWithThrust = (vel0 + velFinalWithThrust) / 2 * timeWithThrust

timeWithoutThrustAscend = (0 - velFinalWithThrust) / g
deltaYAscendWithoutThrust = (0 + velFinalWithThrust) / 2 * timeWithoutThrustAscend
deltaY = deltaYAscendWithThrust + deltaYAscendWithoutThrust
velFinalWithoutThrust = -np.sqrt(2 * np.abs(g) * deltaY)

timeWithoutThrustDescend = np.sqrt(deltaY * 2 / np.abs(g))
timeWithoutThrust = timeWithoutThrustAscend + timeWithoutThrustDescend

totalTime = int(round(timeWithThrust + timeWithoutThrust))

def graph(totalTime, deltaYAscendWithThrust, deltaY):
    for i in range(1, totalTime + 1):
        time.append(i)
        if i <= timeWithThrust:
            accels.append(accel0)
            vels.append(vels[i - 1] + accels[i])
            hs.append(hs[i - 1] + vels[i])
            #hs.append(vels[i] / 2 * i)
        elif i <= timeWithThrust + timeWithoutThrustAscend:
            accels.append(g)
            vels.append(vels[i - 1] + accels[i])
            hs.append(hs[i - 1] + vels[i])
            #hs.append(deltaYAscendWithThrust + vels[i] / 2 * (i - timeWithThrust))
        else:
            accels.append(g)
            vels.append(vels[i - 1] + accels[i])
            hs.append(hs[i - 1] + vels[i])
            #hs.append(deltaY + (vels[i]) / 2 * (i - timeWithThrust - timeWithoutThrustAscend))

    plt.plot(time, hs)
    plt.xlabel("time")
    plt.ylabel("heights")
    plt.show()
    plt.plot(time, vels)
    plt.xlabel("time")
    plt.ylabel("velocities")
    plt.show()
    plt.plot(time, accels)
    plt.xlabel("time")
    plt.ylabel("accelerations")
    plt.show()

graph(totalTime, deltaYAscendWithThrust, deltaY)


