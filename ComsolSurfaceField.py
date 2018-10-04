# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:38:18 2017

@author: wei
"""
# This is not based on data from 20170418_03_GateWireOnlyNewMakeGeo2.mph
# This is based on data from 20170418_04_GateWireOnlyNewMakeGeoMesh01,02.mph
#filestr ="01"
filestr ="02"
workdir ="/media/wei/ACA8-1ECD1/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD1/SystemTest//XenonProperty/")
#sys.path.insert(0, "/home/wei/Dropbox/pythonlib201702/python-lib/lzrd")
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import calendar
import scipy.stats
#import cPickle as cp
import matplotlib.colors as colors
import math
import unit
#import statsmodels.api as sm
#from statsmodels.nonparametric.kernel_regression import KernelReg
#import extrap1d

from matplotlib import colors as mcolors
from cycler import cycler
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
fig, ax = plt.subplots()
color_cycle = list(mpl.rcParams['axes.prop_cycle'])
mpl.rcParams['figure.figsize'] = [8.0, 6.0]
mpl.rcParams['figure.dpi'] = 80
mpl.rcParams['savefig.dpi'] = 100

mpl.rcParams['font.size'] = 14
mpl.rcParams['legend.fontsize'] = 'small'
mpl.rcParams['figure.titlesize'] = 'large'


markers = ['.', ',','o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|' , '_',]# 'P': 'plus_filled', 'X': 'x_filled',# 0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase',}
fignum =20

EFieldOnSurfaceOrigin = np.loadtxt(workdir+"EFieldOnSurfaces"+filestr+".txt", skiprows = 5)
#Opposite z sign
EFieldOnSurfaceOriginOppoZ = np.copy(EFieldOnSurfaceOrigin)
temparray = np.copy(EFieldOnSurfaceOriginOppoZ[:,2]) 
EFieldOnSurfaceOriginOppoZ[:,2] = EFieldOnSurfaceOriginOppoZ[:,3]
EFieldOnSurfaceOriginOppoZ[:,3] = temparray
EFieldOnSurfaceOriginOppoZ[:,4] = EFieldOnSurfaceOriginOppoZ[:,4]
EFieldOnSurfaceOriginOppoZ[:,5] = EFieldOnSurfaceOriginOppoZ[:,5]
EFieldOnSurfaceOriginOppoZ[:,6] = EFieldOnSurfaceOriginOppoZ[:,6]
EFieldOnSurfaceOrigin = np.append(EFieldOnSurfaceOrigin, -EFieldOnSurfaceOriginOppoZ, axis=0)
del temparray, EFieldOnSurfaceOriginOppoZ

Ratio1, sort_index = np.unique(EFieldOnSurfaceOrigin[:,2]/EFieldOnSurfaceOrigin[:,3], return_index=True)
sort_index = np.argsort(EFieldOnSurfaceOrigin[:,2]/EFieldOnSurfaceOrigin[:,3])
EFieldOnSurface1 = EFieldOnSurfaceOrigin[sort_index,:]
V_Top1 = EFieldOnSurface1[:,0]/(EFieldOnSurface1[:,3])
V_Bot1 = EFieldOnSurface1[:,1]/(EFieldOnSurface1[:,3])
E_Top1 = EFieldOnSurface1[:,2]/(EFieldOnSurface1[:,3])
E_Bot1 = EFieldOnSurface1[:,3]/(EFieldOnSurface1[:,3])
E_Wire_Ave1 = EFieldOnSurface1[:,4]/(EFieldOnSurface1[:,3])
E_Wire_Min1 = EFieldOnSurface1[:,5]/(EFieldOnSurface1[:,3])
E_Wire_Max1 = EFieldOnSurface1[:,6]/(EFieldOnSurface1[:,3])
Ratio1 = E_Top1/E_Bot1

Ratio2, sort_index2 = np.unique(EFieldOnSurfaceOrigin[:,2]/(EFieldOnSurfaceOrigin[:,2]-EFieldOnSurfaceOrigin[:,3]), return_index=True)
EFieldOnSurface2 = EFieldOnSurfaceOrigin[sort_index2,:]
V_Top2 = EFieldOnSurface2[:,0]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])
V_Bot2 = EFieldOnSurface2[:,1]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])
E_Top2 = EFieldOnSurface2[:,2]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])
E_Bot2 = EFieldOnSurface2[:,3]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])
E_Wire_Ave2 = EFieldOnSurface2[:,4]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])
E_Wire_Min2 = EFieldOnSurface2[:,5]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])
E_Wire_Max2 = EFieldOnSurface2[:,6]/(EFieldOnSurface2[:,2]-EFieldOnSurface2[:,3])

#Plot Start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
ax1.plot(E_Top1, np.abs(E_Wire_Ave1), "ro-", label = "|E| Field on Wire Surface Average")
ax1.plot(E_Top1, np.abs(E_Wire_Min1), "bo-", label = "|E| Field on Wire Surface Minimum")
ax1.plot(E_Top1, np.abs(E_Wire_Max1), "go-", label = "|E| Field on Wire Surface Maximum")

ax1.set_xlabel("E_Top (unit)")
ax1.set_ylabel("E (unit)")
ax1.set_xlim(-50,50)
ax1.set_ylim(-0,800)

ax1.set_title("Wire Surface Field: E_Bot = 1 unit")

plt.legend(loc=1)
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end

#Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
ax1.plot(E_Top2, np.abs(E_Wire_Ave2), "ro-", label = "|E| Field on Wire Surface Average")
ax1.plot(E_Top2, np.abs(E_Wire_Min2), "bo-", label = "|E| Field on Wire Surface Minimum")
ax1.plot(E_Top2, np.abs(E_Wire_Max2), "go-", label = "|E| Field on Wire Surface Maximum")

ax1.set_xlabel("E_Top (unit)")
ax1.set_ylabel("E (unit)")
ax1.set_xlim(-10,10)
ax1.set_ylim(-5,20)

ax1.set_title("Wire Surface Field: E_Top - E_Bot = 1 unit")

plt.legend(loc=1)
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end

#Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
ax1.plot(E_Top2/E_Bot2, np.abs(E_Wire_Ave2), "ro", label = "|E| Field on Wire Surface Average")
ax1.plot(E_Top2/E_Bot2, np.abs(E_Wire_Min2), "bo", label = "|E| Field on Wire Surface Minimum")
ax1.plot(E_Top2/E_Bot2, np.abs(E_Wire_Max2), "go", label = "|E| Field on Wire Surface Maximum")

ax1.set_xlabel("E_Top /E_Bot")
ax1.set_ylabel("E (unit)")
ax1.set_xlim(-50,50)
ax1.set_ylim(-5,20)

ax1.set_title("Wire Surface Field: E_Top - E_Bot = 1 unit")

plt.legend(loc=1)
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end

plt.show()

EFieldOnSurfaceOrigin = np.loadtxt(workdir+"EFieldOnSurfaces"+filestr+".txt", skiprows = 5)
#Opposite z sign
#EFieldOnSurfaceOriginOppoZ = np.copy(EFieldOnSurfaceOrigin)
#temparray = np.copy(EFieldOnSurfaceOriginOppoZ[:,2]) 
#EFieldOnSurfaceOriginOppoZ[:,2] = EFieldOnSurfaceOriginOppoZ[:,3]
#EFieldOnSurfaceOriginOppoZ[:,3] = temparray
#EFieldOnSurfaceOriginOppoZ[:,4] = EFieldOnSurfaceOriginOppoZ[:,4]
#EFieldOnSurfaceOriginOppoZ[:,5] = EFieldOnSurfaceOriginOppoZ[:,5]
#EFieldOnSurfaceOriginOppoZ[:,6] = EFieldOnSurfaceOriginOppoZ[:,6]
#EFieldOnSurfaceOrigin = np.append(EFieldOnSurfaceOrigin, -EFieldOnSurfaceOriginOppoZ, axis=0)
#del temparray, EFieldOnSurfaceOriginOppoZ

Ratio1, sort_index = np.unique(EFieldOnSurfaceOrigin[:,2]/EFieldOnSurfaceOrigin[:,3], return_index=True)
sort_index = np.argsort(EFieldOnSurfaceOrigin[:,2]/(EFieldOnSurfaceOrigin[:,3]))
#sort_index = np.array([0])
EFieldOnSurface1 = EFieldOnSurfaceOrigin[sort_index,:]
V_Top = EFieldOnSurface1[:,0]
V_Bot = EFieldOnSurface1[:,1]
V_Top1 = EFieldOnSurface1[:,0]/(EFieldOnSurface1[:,3])
V_Bot1 = EFieldOnSurface1[:,1]/(EFieldOnSurface1[:,3])
E_Top1 = EFieldOnSurface1[:,2]/(EFieldOnSurface1[:,3])
E_Bot1 = EFieldOnSurface1[:,3]/(EFieldOnSurface1[:,3])
E_Wire_Ave1 = EFieldOnSurface1[:,4]/(EFieldOnSurface1[:,3])
E_Wire_Min1 = EFieldOnSurface1[:,5]/(EFieldOnSurface1[:,3])
E_Wire_Max1 = EFieldOnSurface1[:,6]/(EFieldOnSurface1[:,3])
Ratio1 = E_Top1/E_Bot1






#Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)

for ii in range(len(E_Bot1)):
    print EFieldOnSurfaceOrigin[ii,0],EFieldOnSurfaceOrigin[ii,2]/EFieldOnSurfaceOrigin[ii,3]
    plt.plot(EFieldOnSurfaceOrigin[ii,2]/EFieldOnSurfaceOrigin[ii,3], EFieldOnSurfaceOrigin[ii,0],"ro")
ax1.set_xlim(10,30)
#ax1.set_ylim(-5,20)   
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1  
  #Plot end  
    
    