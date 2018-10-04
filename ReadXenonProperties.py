# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

workdir ="/media/wei/ACA8-1ECD/SystemTest/"
import sys
#sys.path.insert(0, "/home/wei/Dropbox/pythonlib201702/python-lib/lzrd")
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import calendar
import scipy.stats
import cPickle as cp
import matplotlib.colors as colors
import math
#import statsmodels.api as sm
#from statsmodels.nonparametric.kernel_regression import KernelReg
#import extrap1d
from scipy import interpolate
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



XenonSaturationTableHeader = np.array(["Temperature (K)",	"Pressure (MPa)","	Density (l, mol/l)",	
                "Volume (l, l/mol)", "Internal Energy (l, kJ/mol)",	"Enthalpy (l, kJ/mol)",	
                "Entropy (l, J/mol*K)", "Cv (l, J/mol*K)",	"Cp (l, J/mol*K)",	
                "Sound Spd. (l, m/s)", "Joule-Thomson (l, K/MPa)",	"Viscosity (l, uPa*s)",	
                "Therm. Cond. (l, W/m*K)", "Surf. Tension (l, N/m)",	"Density (v, mol/l)",	
                "Volume (v, l/mol)", "Internal Energy (v, kJ/mol)",	"Enthalpy (v, kJ/mol)",	
                "Entropy (v, J/mol*K)", "Cv (v, J/mol*K)",	"Cp (v, J/mol*K)",	
                "Sound Spd. (v, m/s)", "Joule-Thomson (v, K/MPa)",	"Viscosity (v, uPa*s)",	
                "Therm. Cond. (v, W/m*K)"])

Xenon300KTableHeader = np.array(["Temperature (K)",	"Pressure (MPa)",	"Density (mol/l)",
                                 "Volume (l/mol)",	"Internal Energy (kJ/mol)",	"Enthalpy (kJ/mol)"
                                 "Entropy (J/mol*K)",	"Cv (J/mol*K)",	"Cp (J/mol*K)",	
                                 "Sound Spd. (m/s)",	"Joule-Thomson (K/MPa)",	"Viscosity (uPa*s)",	
                                 "Therm. Cond. (W/m*K)",	"Phase"])

XenonSaturationTable= np.loadtxt(workdir+"/XenonProperty/XenonSaturation.txt", skiprows=1)
Xenon300KTable = np.empty([0,len(Xenon300KTableHeader)])
with open(workdir+"/XenonProperty/Xenon300K.txt") as f:
    next(f)
    for line in f:
        content = line.split("\t")
        content = [float(x) for x in content[:-1]] 
        Xenon300KTable= np.append(Xenon300KTable, np.array([content]), axis=0)

Xenon290KTable = np.empty([0,len(Xenon300KTableHeader)])
with open(workdir+"/XenonProperty/Xenon290K.txt") as f:
    next(f)
    for line in f:
        content = line.split("\t")
        content = [float(x) for x in content[:-1]] 
        Xenon290KTable= np.append(Xenon290KTable, np.array([content]), axis=0)
        
Xenon310KTable = np.empty([0,len(Xenon300KTableHeader)])
with open(workdir+"/XenonProperty/Xenon310K.txt") as f:
    next(f)
    for line in f:
        content = line.split("\t")
        content = [float(x) for x in content[:-1]] 
        Xenon310KTable= np.append(Xenon310KTable, np.array([content]), axis=0)



#### Plot 1 start.
a=plt.figure(1, figsize=(9,7))
ax1=plt.subplot(1,1,1)
SelectSaturationTableTemp = 0
SelectSaturationTablePres = 1
SelectSaturationTableDensLiq = 2
SelectSaturationTableDensVap =14
ax1.plot(XenonSaturationTable[:, SelectSaturationTableDensVap], XenonSaturationTable[:,SelectSaturationTableTemp], label = "Saturation Vapor Phase", color = 'b')
#ax1.plot(XenonSaturationTable[:, SelectSaturationTableDensLiq], XenonSaturationTable[:,SelectSaturationTableTemp], label = "Saturation Liquid Phase", color = 'g')
ax1.set_ylim(173.5,180)
ax1.set_xlabel("Density (mol/l)")
ax1.set_ylabel("Temperature (K)")
plt.legend(loc=4)
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(Xenon300KTable[:, SelectSaturationTableDensLiq], Xenon300KTable[:,SelectSaturationTablePres], label = "300 K", color = 'r')
ax2.set_ylim(.286,.3825)
ax2.set_ylabel("Pressure (MPa)")
plt.legend(loc =1)

plt.title("Xenon Density on Saturation Curve and 300 K")
ax1.set_xlim(.11, .16)
plt.savefig(workdir+"/XenonProperty//1"+".png")
#### Plot 1 end.

#### Plot 2 start.
a=plt.figure(2, figsize=(9,7))
ax1=plt.subplot(1,1,1)
SelectSaturationTableTemp = 0
SelectSaturationTablePres = 1
SelectSaturationTableDensLiq = 2
SelectSaturationTableDensVap =14
ax1.plot(XenonSaturationTable[:, SelectSaturationTableDensVap], XenonSaturationTable[:,SelectSaturationTablePres], label = "Saturation Vapor Phase", color = 'b')
#ax1.plot(XenonSaturationTable[:, SelectSaturationTableDensLiq], XenonSaturationTable[:,SelectSaturationTableTemp], label = "Saturation Liquid Phase", color = 'g')
ax1.set_ylim(.16,.22)
ax1.set_xlabel("Density (mol/l)")
ax1.set_ylabel("Pressure (MPa) for Saturation Curve")
plt.legend(loc=4)
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(Xenon300KTable[:, SelectSaturationTableDensLiq], Xenon300KTable[:,SelectSaturationTablePres], label = "300 K", color = 'r')
ax2.set_ylim(.285,.380)
ax2.set_ylabel("Pressure (MPa) for T = 300K")
plt.legend(loc =1)

plt.title("Xenon Density on Saturation Curve and 300 K")
ax1.set_xlim(.11, .16)
plt.savefig(workdir+"/XenonProperty//2"+".png")
#### Plot 2 start.

#### Plot 3 start.
fignum=3
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
SelectSaturationTableTemp = 0
SelectSaturationTablePres = 1
SelectSaturationTableDensLiq = 2
SelectSaturationTableDensVap =14
ax1.plot(XenonSaturationTable[:, SelectSaturationTableDensVap], XenonSaturationTable[:,SelectSaturationTablePres], label = "Saturation Vapor Phase", color = 'b')
#ax1.plot(XenonSaturationTable[:, SelectSaturationTableDensLiq], XenonSaturationTable[:,SelectSaturationTableTemp], label = "Saturation Liquid Phase", color = 'g')
#ax1.set_ylim(.16,.22)
ax1.set_xlabel("Density (mol/l)")
#ax1.set_ylabel("Pressure (MPa) for Saturation Curve")
plt.legend(loc=4)
ax1.grid(True)
#ax1 = ax1.twinx()
ax1.plot(Xenon310KTable[:, SelectSaturationTableDensLiq], Xenon310KTable[:,SelectSaturationTablePres], label = "310 K", color = 'm')
ax1.plot(Xenon300KTable[:, SelectSaturationTableDensLiq], Xenon300KTable[:,SelectSaturationTablePres], label = "300 K", color = 'r')
ax1.plot(Xenon290KTable[:, SelectSaturationTableDensLiq], Xenon290KTable[:,SelectSaturationTablePres], label = "290 K", color = 'g')
ax1.set_ylim(.16,.4)
ax1.set_ylabel("Pressure (MPa)")

plt.axvline(0.11595, color="k", linestyle = ":", label="LZ low limit")
plt.axvline(0.15546, color="k", linestyle = ":", label="LZ high limit")
plt.axvline(0.12922, color="k", linestyle = "-", label="LZ baseline")
plt.legend(loc =2)

plt.title("Xenon Density on Saturation Curve and Constant Temperature")
ax1.set_xlim(.11, .16)
plt.savefig(workdir+"/XenonProperty/"+str(fignum)+".png")

#### Plot 3 start.


plt.show()
