# Program for the measuring temperture as a function of time
# 21/03/2024

import eyes17.eyes
p = eyes17.eyes.open()
import time, math
import numpy as np


R0=1000                             # PT1000
Alpha=3.85
t0=time.time()                      # Time initialization

while True:                         # For Contineous measurement
   n=10                             # For Averaging 
   Rsum=0                       
   for x in range (0,n):            # Loop for averaging
       r=p.get_resistance()         # Measure the resistance in ohm
       Rsum=Rsum+r                  # Sum of resistance
   R=Rsum/n                         # Average resistance

   T = 1000*(1/Alpha)*((R/R0)-1)    # Calculate Temperature from Resistance
   ts=time.time()                   # time stamp
   time.sleep(1.0)                  # Wait for 1 sec
   t=ts-t0                          # current time
   
   print("%4.2f" % t, "S", "  ","%4.1f" % T,"°C")
   file = open ("Water Cooling.dat", "a") # Appending file
   file.write("{0:4.2f} {1:4.1f}\n".format(t,T)) 
file.close()
