# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:09:19 2017

@author: wei
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

import ReadXenonProperties
import unit

fignum=10
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
#plt.axvline(0.11595, color="k", linestyle = ":", label="LZ low limit")
#plt.axvline(0.15546, color="k", linestyle = ":", label="LZ high limit")
#plt.axvline(0.12922, color="k", linestyle = "-", label="LZ baseline")

alpha = .137 #ph/e/V
beta = -4.71e-18*(1.e-2)**2 #ph/e*m^2/atom
d= 13*m
dVArray = np.arange(0, 16, 1)*k
NArray  = np.linspace(0.11,0.16, 6)
NArrayReal = NArray*NA*1.e3
for n in NArray:
    N = n*NA*1.e3
    EOverN= dVArray/d/N
    dLdx = alpha* EOverN + beta
    L = dLdx *d*N
    plt.plot(dVArray , L, label= str(n)+ "(mol/l)")
ax1.set_xlabel("dV (V)")
ax1.set_ylim(0,1500)
plt.legend(loc=4)
ax1.grid(True)
#ax1.set_ylabel("Pressure (MPa) for Saturation Curve")
plt.savefig(workdir+"/XenonProperty/"+str(fignum)+".png")


plt.show()