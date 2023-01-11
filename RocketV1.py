import math
import matplotlib.pyplot as plt
# constants
g = 9.81 # acceleration due to gravity in m/s^2
Rdry = 287.058 # specific gas constant for dry air in J/(kg * K)
Rv = 461.495 # specific gas constant for water vapor in J/(kg * K)
CConstant = 273.15
Cv = 0.97 # the velocity coefficient
rhoWater = 1000 # water density in kg/m^3
Pbaro = 10000 # current barometric pressure in pascals
Cc = 0.9 # contraction coefficient
# inputs
Ft = 15 # force due to thrust in N
temp = 20 + 273.15 # temperature in Kelvin (ambient air)
phi = 0.5 # relative humidity
Af = math.pi * (0.54 ** 2) # frontal area of the rocket in m^2
Av = math.pi * (0.25 ** 2) # area of bottle neck opening
Cd = 0.295 # coefficient of drag
deltaT = 0.005 # instant change in time
# calculations regarding the environment
Psat = 0.61121 * (math.e ** ((18.678 - ((temp - CConstant) / 234.5)) * ((temp - CConstant) / (257.14 + temp - CConstant)))) # saturation vapor pressure of water (Arden Buck Equation)
rhoA = ((Pbaro - phi * Psat) / (Rdry * temp)) + ((phi * Psat) / (Rv * temp)) # air density in kg/m^3
# initial values
initialM = 1 # mass in kg
initialVel = 0 # initial velocity of rocket in m/s
initialFd = 0.5 * rhoA * (initialVel ** 2) * Cd * Af # force drag against motion due to air resistance in N
initialForce = Ft - initialM * g + initialFd
initialAccel = initialForce / initialM
initialG = g + initialAccel
initialH = 0.25 # the height of water above the nozzle opening
initialP = 3500000 - Pbaro # the excess pressure in the tank above ambient pressure in Pa
mPrime = Cc * rhoWater * Av # assume constant
initialVWater = Cv * math.sqrt(2 * ((initialG * initialH) + (initialP / rhoWater))) # velocity of the water from the nozzle in m/s
#initializing lists
times = [] # a list containing all the time steps
accels = [] # a list containing all the accelerations
vels = [] # a list containing all the velocities
alts = [] # a list containing all the altitudes
Gs = [] # a list containing all the Gs (total acceleration)
Hs = [] # a list containing all the Hs
Fds = [] # a list containing all the Fds
masses = [] # a list containing all the masses
forces = [] # a list containing all the forces
ps = [] # a list containing all the excess pressures
Fts = [] # a list containing all the force of thrust
# append initial values
times.append(0)
accels.append(initialAccel)
vels.append(0)
alts.append(0)
Gs.append(initialG)
Hs.append(initialH)
Fds.append(initialFd)
masses.append(initialM)
forces.append(initialForce)
ps.append(initialP)
Fts.append(Ft)
def graph(deltaT):
  i = 0
  instantAlt = alts[i]
 
  while instantAlt >= 0:
      times.append(times[i] + deltaT)
      newMass = masses[i] - mPrime * deltaT
      if newMass > 0:
           masses.append(newMass)
      else:
           masses.append(0.01)
 
      vels.append(vels[i] + (accels[i] * deltaT))
      alts.append(alts[i] + vels[i] * times[i + 1] + 0.5 * accels[i] * (deltaT ** 2))
      Fds.append(0.5 * rhoA * vels[i + 1] * (vels[i + 1] ** 2) * Cd * Af)
      #Fts.append(masses[i + 1] * vels[i + 1] - masses[i] * vels[i])
 
      if vels[i + 1] > 0:
           forces.append(Ft - masses[i] * g - Fds[i])
      else:
           forces.append(Ft - masses[i] * g + Fds[i])
 
      accels.append(forces[i + 1] / masses[i + 1])
      ps.append(forces[i + 1] / (math.pi * (0.25 ** 2)))
      Fts.append(ps[i + 1] * (math.pi * (0.25 ** 2)))
      i = i + 1
      instantAlt = alts[i]
  print(times)
  print(alts)
  print(vels)
  print(accels)
  print(Fds)
  print(masses)
  print(forces)
  plt.scatter(times, alts)
  plt.xlabel("time (s)")
  plt.ylabel("altitudes (m)")
  plt.show()
  plt.scatter(times, vels)
  plt.xlabel("time (s)")
  plt.ylabel("velocities (m/s)")
  plt.show()
  plt.scatter(times, accels)
  plt.xlabel("time (s)")
  plt.ylabel("accelerations (m/s^2)")
  plt.show()
 
graph(deltaT)
# does not reach a uniform end time with different deltaT
