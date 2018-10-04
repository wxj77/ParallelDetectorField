# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:38:18 2017

@author: wei
"""
# This is based on data from 20170418_04_GateWireOnlyNewMakeGeoMeshGridFactor.mph

workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
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
import scipy.optimize as opt

fig, ax = plt.subplots()
color_cycle = list(mpl.rcParams['axes.prop_cycle'])
mpl.rcParams['figure.figsize'] = [8.0, 6.0]
mpl.rcParams['figure.dpi'] = 80
mpl.rcParams['savefig.dpi'] = 100

mpl.rcParams['font.size'] = 14
mpl.rcParams['legend.fontsize'] = 'small'
mpl.rcParams['figure.titlesize'] = 'large'


markers = ['.', ',','o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|' , '_',]# 'P': 'plus_filled', 'X': 'x_filled',# 0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase',}
fignum =100

def f_test(DoverA, a0, d0):
    return a0*1./(2.*np.pi)*np.log(1./(np.pi*DoverA*d0/a0))

def f_test1(DoverA, a0):
    d0=1.
    return a0*1./(2.*np.pi)*np.log(1./(np.pi*DoverA*d0/a0))

def f_test2(DoverA, d0):
    a0=0.5
    return a0*1./(2.*np.pi)*np.log(1./(np.pi*DoverA*d0/a0))

EFieldOnSurfaceOrigin = np.loadtxt(workdir+"EFieldOnSurfacesWovenGridFactor1.txt", skiprows = 5)
Dis_Top_Grid1 = 2.* unit.c
Radius1, sort_index = np.unique(EFieldOnSurfaceOrigin[:,0], return_index=True)
Radius1 = Radius1 *unit.u
EFieldOnSurface1 = EFieldOnSurfaceOrigin[sort_index,:]
E_Top1 = EFieldOnSurface1[:,5]
E_Bot1 = EFieldOnSurface1[:,6]
V_Top1 = EFieldOnSurface1[0,1]
V_Bot1 = EFieldOnSurface1[0,2]
V_Gate1 = EFieldOnSurface1[0,3]
Pitch_Gate1 = EFieldOnSurface1[0,4]*unit.m

E_Dif1 = E_Top1 -E_Bot1 
V0_Gate1 = V_Top1 + E_Top1* Dis_Top_Grid1
GridFactor1 =  - (V0_Gate1 - V_Gate1)/E_Dif1/Pitch_Gate1
dOvera1 = 2.* Radius1/Pitch_Gate1
#del E_Top1, E_Bot1

EFieldOnSurfaceOrigin = np.loadtxt(workdir+"EFieldOnSurfacesWovenGridFactor2.txt", skiprows = 5)
Dis_Top_Grid2 = 2.* unit.c
Radius2, sort_index = np.unique(EFieldOnSurfaceOrigin[:,0], return_index=True)
Radius2 = Radius2 *unit.u
EFieldOnSurface2 = EFieldOnSurfaceOrigin[sort_index,:]
E_Top2 = EFieldOnSurface2[:,5]
E_Bot2 = EFieldOnSurface2[:,6]
V_Top2 = EFieldOnSurface2[0,1]
V_Bot2 = EFieldOnSurface2[0,2]
V_Gate2 = EFieldOnSurface2[0,3]
Pitch_Gate2 = EFieldOnSurface2[0,4]*unit.m

E_Dif2 = E_Top2 -E_Bot2 
V0_Gate2 = V_Top2 + E_Top2* Dis_Top_Grid2
GridFactor2 =  - (V0_Gate2 - V_Gate2)/E_Dif2/Pitch_Gate2
dOvera2 = 2.* Radius2/Pitch_Gate2
#del E_Top1, E_Bot1

EFieldOnSurface1 = np.loadtxt(workdir+"EFieldOnSurfaces_bk.txt", skiprows = 5)
Dis_Top_Grid3 = 1.* unit.c
Radius3 = 37.5 * unit.u
E_Top3 = EFieldOnSurface1[:,2]
E_Bot3 = EFieldOnSurface1[:,3]
V_Top3 = EFieldOnSurface1[:,0]
V_Bot3 = EFieldOnSurface1[:,1]
V_Gate3 = 0.
Pitch_Gate3 = 5.*unit.m

E_Dif3 = E_Top3 -E_Bot3 
V0_Gate3 = V_Top3 + E_Top3* Dis_Top_Grid3
GridFactor3 =  - (V0_Gate3 - V_Gate3)/E_Dif3/Pitch_Gate3
dOvera3 = 2.* Radius3/Pitch_Gate3*np.ones_like(GridFactor3)


F_pw_Sim= np.array([0.58590372163, 0.47576841662, 0.41118984985, 0.36531875035, 0.32968814794,\
	0.30053234318, 0.27584103705, 0.25442035471, 0.23549110386, 0.21852468108, ])

#F_cal = 1/(2*np.pi)*log(a/(np.pi*d))
DoverA_pw_Sim =np.array([0.008, 0.016, 0.024, 0.032, 0.040, 0.048, 0.056, 0.064, 0.072, 0.080, ])

F_ww_Sim= np.array([0.38948626045, 0.33626300714, \
	0.27997136356, 0.22259265433, 0.18849029185, 0.16396351557, 0.14464332436,\
	0.12868768532, 0.11501896114, 0.10301846239, 0.09229970937, 0.08257406154,])

DoverA_ww_Sim =np.array([	0.002, 0.004, \
			0.008, 0.016, 0.024, 0.032, 0.040, 0.048, 0.056, 0.064, 0.072, 0.080 ])



# Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
popt_ww, pcov_ww = opt.curve_fit(f_test, dOvera1, GridFactor1, p0=[.5,1])

#ax1.plot(DoverA_pw_Sim, F_pw_Sim, "ko", linewidth=6, label="Parallel Wire Sim")
#ax1.plot(DoverA_ww_Sim, F_ww_Sim, "ko", linewidth=6, label="Wowen Wire Sim")

ax1.plot(dOvera1, 1./(2.*np.pi)*np.log(1./(np.pi*dOvera1)), "g:", linewidth=4, label="Parallel Wire Prediction")
ax1.plot(dOvera1, GridFactor1, "bo", linewidth=4, label="Wowen Wire Sim 1")
ax1.plot(dOvera2, GridFactor2, "ro", linewidth=4, label="Wowen Wire Sim 2")
ax1.plot(dOvera3, GridFactor3, "mo", linewidth=4, label="Wowen Wire Sim 3")
dOvera = np.linspace(0,0.08,101)
ax1.plot(dOvera, 1./2.*1./(2.*np.pi)*np.log(1./(np.pi*dOvera*2.)), "k:", linewidth=4, label="Wowen Wire Prediction\n"+r"$\frac{0.5}{2\pi}*\ln\frac{0.5 a}{\pi d}$")

ax1.plot(dOvera, 1./2.*1./(2.*np.pi)*np.log(1./(np.pi*dOvera)), "k--", linewidth=4, label="Wowen Wire Prediction\n"+r"$\frac{0.5}{2\pi}*\ln\frac{0.5 a}{\pi 0.5 d}$")

ax1.plot(dOvera1, f_test(dOvera1, *popt_ww), "c:", linewidth=1, label="Wowen Wire Prediction Better\n"+r"$\frac{%.4f}{2\pi}*\ln\frac{%.4f a}{\pi %.4f d}$"%(popt_ww[0],popt_ww[0],popt_ww[1])+"")

##Section start.
EFieldOnSurfaceOrigin = np.loadtxt(workdir+"EFieldOnSurfacesWovenGridFactor01.txt", skiprows = 5)
Dis_Top_Grid1 = 2.* unit.c
Radius1, sort_index = np.unique(EFieldOnSurfaceOrigin[:,0], return_index=True)
Radius1 = Radius1 *unit.u
EFieldOnSurface1 = EFieldOnSurfaceOrigin[sort_index,:]
E_Top1 = EFieldOnSurface1[:,5]
E_Bot1 = EFieldOnSurface1[:,6]
V_Top1 = EFieldOnSurface1[0,1]
V_Bot1 = EFieldOnSurface1[0,2]
V_Gate1 = EFieldOnSurface1[0,3]
Pitch_Gate1 = EFieldOnSurface1[0,4]*unit.m
E_Dif1 = E_Top1 -E_Bot1 
V0_Gate1 = V_Top1 + E_Top1* Dis_Top_Grid1
GridFactor1 =  - (V0_Gate1 - V_Gate1)/E_Dif1/Pitch_Gate1
dOvera1 = 2.* Radius1/Pitch_Gate1
#del E_Top1, E_Bot1
ax1.plot(dOvera1, GridFactor1, "b-", linewidth=4, label="Wowen Wire Sim New 1")
popt_ww, pcov_ww = opt.curve_fit(f_test, dOvera1, GridFactor1, p0=[.5,1])
ax1.plot(dOvera1, f_test(dOvera1, *popt_ww), "c:", linewidth=1, label="Wowen Wire Prediction Better\n"+r"$\frac{%.4f}{2\pi}*\ln\frac{%.4f a}{\pi %.4f d}$"%(popt_ww[0],popt_ww[0],popt_ww[1])+"")
##Section end.

##Section start.
EFieldOnSurfaceOrigin = np.loadtxt(workdir+"EFieldOnSurfacesMeshGridFactor01.txt", skiprows = 5)
Dis_Top_Grid1 = 2.* unit.c
Radius1, sort_index = np.unique(EFieldOnSurfaceOrigin[:,0], return_index=True)
Radius1 = Radius1 *unit.u
EFieldOnSurface1 = EFieldOnSurfaceOrigin[sort_index,:]
E_Top1 = EFieldOnSurface1[:,5]
E_Bot1 = EFieldOnSurface1[:,6]
V_Top1 = EFieldOnSurface1[0,1]
V_Bot1 = EFieldOnSurface1[0,2]
V_Gate1 = EFieldOnSurface1[0,3]
Pitch_Gate1 = EFieldOnSurface1[0,4]*unit.m
E_Dif1 = E_Top1 -E_Bot1 
V0_Gate1 = V_Top1 + E_Top1* Dis_Top_Grid1
GridFactor1 =  - (V0_Gate1 - V_Gate1)/E_Dif1/Pitch_Gate1
dOvera1 = 2.* Radius1/Pitch_Gate1
#del E_Top1, E_Bot1
ax1.plot(dOvera1, GridFactor1, "b-", linewidth=4, label="Wowen Wire Sim New 1")
popt_ww, pcov_ww = opt.curve_fit(f_test, dOvera1, GridFactor1, p0=[.5,1])
ax1.plot(dOvera1, f_test(dOvera1, *popt_ww), "c:", linewidth=1, label="Wowen Wire Prediction Better\n"+r"$\frac{%.4f}{2\pi}*\ln\frac{%.4f a}{\pi %.4f d}$"%(popt_ww[0],popt_ww[0],popt_ww[1])+"")
popt_ww, pcov_ww = opt.curve_fit(f_test1, dOvera1, GridFactor1, p0=[1])
#ax1.plot(dOvera1, f_test1(dOvera1, *popt_ww), "y:", linewidth=4, label="Wowen Wire Prediction Better\n"+r"$\frac{%.4f}{2\pi}*\ln\frac{%.4f a}{\pi d}$"%(popt_ww[0], popt_ww[0])+"")
popt_ww, pcov_ww = opt.curve_fit(f_test2, dOvera1, GridFactor1, p0=[1])
ax1.plot(dOvera1, f_test2(dOvera1, *popt_ww), "m:", linewidth=4, label="Wowen Wire Prediction Better\n"+r"$\frac{0.5}{2\pi}*\ln\frac{0.5 a}{\pi %.4f d}$"%(popt_ww[0])+"")
##Section end.
##Section end.

ax1.axvline(0.1/2.5, color= "r", linewidth=2,label="LZ Anode: 0.1 mm/2.5 mm")
ax1.axvline(0.075/5., color= "g", linewidth=2,label="LZ Gate, LZ Bottom: 0.075 mm/5 mm")
ax1.axvline(0.1/5., color= "b", linewidth=2,label="LZ Cathode: 0.1 mm/5 mm")
#ax.axvline(0.075/5., color= "k", linewidth=2,label="LZ Bottom: 0.075 mm/5 mm")


ax1.set_xlabel("d/a ")
ax1.set_ylabel("Grid Factor")
#ax1.set_xlim(-50,50)
#ax1.set_xlim(-1,1)
ax1.set_ylim(0.,0.6)

ax1.set_title("Grid Factor")

#plt.legend(loc=1)
# Shrink current axis by 20%
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
# Plot end

