"""
FLIP TIME ANALYSIS
"""

'''
LOOK AT X AND -X TO GIVE AN IDEA OF NUMERICAL ACCURACY
'''
import numpy as np
import math
from Oscillator_class import Oscillator
from System import System
import pandas as pd

m1 = 1
m2 = 1
l1 = 0.1
l2 = 0.1
pend1 = Oscillator(m1,l1)
pend2 = Oscillator(m2,l2)

time = 500000
timestep = 0.002

data=[]
for angle1 in np.linspace(-np.pi,np.pi,200): 
    for angle2 in np.linspace(-np.pi,np.pi,200):
        Z = [angle1,angle2,0,0]
        Sys= System(pend1,pend2)
        Sys.set_initial(Z)
        for step in range(time):
            if 2*np.cos(angle1) + np.cos(angle2) > 1:
                break
            Sys.RK(timestep)
            if abs(Sys.Z[0]) > np.pi or abs(Sys.Z[1]) > np.pi:
                    break 
        print("Point %s.%s finished" %(angle1,angle2))
        if Sys.Z[0] >np.pi:
            data.append([angle1,angle2,timestep*step,'pend1'])
        elif Sys.Z[1] >np.pi:
            data.append([angle1,angle2,timestep*step,'pend2'])
        else:
            data.append([angle1,angle2,timestep*step,'none'])
df = pd.DataFrame(data,columns=['ANGLE 1','ANGLE 2','TIME TO FLIP','WHICH ONE'])
df.to_pickle('ttf_full_0_002_long_abs.csv')