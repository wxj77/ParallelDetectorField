# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 23:12:57 2017

@author: wei
"""
# This is based on data from 20170418_03_GateWireOnlyNewMakeGeo2.mph
fignum = 60
import matplotlib.ticker as tck
workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
from ComsolSurfaceFieldDetail import *
import scipy.integrate as integ
from ElectronCurrentFunctions import *

XMin = 0
XMax = Pitch_Gate
YMin = Radius_Gate * -np.pi
YMax = Radius_Gate * np.pi
RatePerAreaList = []
RatePerAreaListAdderley = []
RatePerAreaListBastaniNejad = [] 
DriftField =.3*unit.k/unit.c#kV/cm
for ii in range(len(E_Bot1)): 
#for ii in range(1):
    SurfaceFieldFunc = interpolate.interp2d(grid_x1, grid_y1, grid_z1[:,:,ii], kind='linear')
    # X, Y, Array_ER[:,ii]    
    #value = integ.dblquad(lambda y, x: ElectronCurrentBastaniNejad(-SurfaceFieldFunc(x,y)*0.3*unit.k/unit.c),XMin, XMax, lambda x: YMin, lambda x: YMax)

    values= (np.vectorize
(ElectronCurrentAdderley)(-np.sign(Ratio1[ii]-1.)*SurfaceFieldFunc(array_x1.flatten(),array_y1.flatten())*DriftField))    
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())  
    RatePerAreaListAdderley.append(value)
    
    values= (np.vectorize
(ElectronCurrentBastaniNejad)(-np.sign(Ratio1[ii]-1.)*SurfaceFieldFunc(array_x1.flatten(),array_y1.flatten())*DriftField))    
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())    
    RatePerAreaListBastaniNejad.append(value)

    values= (np.vectorize
(ElectronCurrent)(-np.sign(Ratio1[ii]-1.)*SurfaceFieldFunc(array_x1.flatten(),array_y1.flatten())*DriftField))    
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())  
    RatePerAreaList.append(value)
      
scale = 0.158877756165
# Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
ax1.plot(E_Top1*DriftField/unit.k*unit.c,np.array(RatePerAreaList)*scale, "ro-", label = "method 1")
ax1.plot(E_Top1*DriftField/unit.k*unit.c,np.array(RatePerAreaListAdderley)*scale, "bo-", label = "Adderley")
ax1.plot(E_Top1*DriftField/unit.k*unit.c,np.array(RatePerAreaListBastaniNejad)*scale, "go-", label = "BastaniNejad")

ax1.set_yscale('log')
ax1.set_xlabel("E_Extraction (kV/cm)")
#ax1.set_ylabel(r"$s^{-1}m^{-2}$")
ax1.set_ylabel(r"$s^{-1}$")
ax1.set_xlim(0,10)
ax1.set_ylim(1.e0,1.e20)

ax1.set_title("Rate in LZ: E_Drift = %.2f kV/cm\n Pitch_Gate = 5 mm, Radius_Gate =37.5 um\n "%(DriftField/unit.k*unit.c))

plt.legend(loc=1)
ax1.grid(True)
ax1.set_position([0.2,0.2, 0.7, 0.6])

#ax2 = ax1.twinx()
#ax2.set_ylim(ax1.get_ylim())
#ax2.set_position(ax1.get_position())
#ax2.yaxis.set_t(ax2.yaxi)

plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end






array_ratio1 = np.linspace(-100,100,41)
grid_x1, grid_y1, grid_ratio1 = np.meshgrid(array_x1,array_y1,array_ratio1)
EFieldPoints = np.empty([0,3])
EFieldValues = np.empty([0,0])
for ii in range(len(E_Bot1)):
    EFieldPoints = np.append(EFieldPoints, np.array([X,Y,np.ones_like(X)*Ratio1[ii]]).T,axis =0)
    EFieldValues = np.append(EFieldValues, Array_ER[:,ii])
#grid_z3 = griddata(points, values, (grid_x1, grid_y1, grid_ratio1), method='linear')


def SurfaceFieldFunction(x):
    return interpolate.LinearNDInterpolator(EFieldPoints, EFieldValues, x)
 


plt.show()   