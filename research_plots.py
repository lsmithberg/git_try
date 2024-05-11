#make plots of M against R, J, and I for polytropic and BSk21

# Imports
# ------------------------------------------------
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
# ------------------------------------------------

# Constants
# ------------------------------------------------
K=5.38e9 #cgs # polytrope K
n=(1.5) # polytropic index
exponent = ((n+1)/n)
G=6.6743e-8 # Newton's constant
c=2.9979e10 # Speed of light
#Put these in cgs
# ------------------------------------------------

#Read in and plot m r and j for BSk21

R = []
M = []
J = []
I = []

import csv
rows = []
with open("mass-radius(BSk21).csv", 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        R.append(float(row[0]))
        M.append(float(row[1]))
        J.append(float(row[2]))
        I.append(float(row[3]))

#read in and plot m r and j for polytropic


R2 = []
M2 = []
J2 = []
I2 = []

import csv
rows = []
with open("mass-radius(polytropic).csv", 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        R2.append(float(row[0]))
        M2.append(float(row[1]))
        J2.append(float(row[2]))
        I2.append(float(row[3]))

#Cut out values past max
L = len(R)
while L>19:
    R.pop(L-1)
    M.pop(L-1)
    J.pop(L-1)
    I.pop(L-1)
    L = len(R)

#???
L = len(R2)
while L>17:
    R2.pop(L-1)
    M2.pop(L-1)
    J2.pop(L-1)
    I2.pop(L-1)
    L = len(R2)
#not sure whether to keep this


#replace this with whichever plot I want to make:
#Plot R and M (combined)

#plt.plot(R2,M2,'ob')
plt.plot(R2,M2)

#plt.plot(R,M,'or')
plt.plot(R,M)

plt.xlabel("R (km)")
plt.ylabel("M/M$_\odot$")

#plt.legend(['Polytropic', '', 'BSk21', ''])
plt.legend(['Polytropic', 'BSk21'])


#plt.xlim(3.5,19)
plt.ylim(0,2.5)
plt.show()



