# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 04:20:11 2018

@author: wei
"""
workdir ="/media/wei/ACA8-1ECD1/ComsolGeoFile/"
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x_list = [1.4, 29.3, 60, 75.4, 90.7]
y_list = [10,20, 50, 275, 664]
#x_list = [0.000000000000000000e+00 ,4.000000000000000000e+00 ,8.000000000000000000e+00 ,1.000000000000000000e+01 ,1.200000000000000000e+01,\
#]# 1.000000000000000000e+01, 1.200000000000000000e+01,]# 1.200000000000000000e+01 1.000000000000000000e+01 8.000000000000000000e+00 0.000000000000000000e+00
y_list = [2.111358941241022968e+00, 7.053742319304324937e+00, 6.249223316562846975e+01, 2.839957688605557564e+02, 6.559966838547505859e+02,\
]# 4.057824827754611192e+02, 7.025369364592752390e+02,]# 3.988916975883989835e+01 3.322346776949719072e+01 2.703850893736118266e+01 2.019659017676484147e+00
erry_list= [1.111241548021590919e-01, 2.065714581695952679e-01, 6.398783046081877313e-01, 1.529757983252979070e+00, 2.904973026225984523e+00,\
]# 2.571180612195781201e+00, 3.078815855689061909e+00,]# 7.711022006873752277e-01 6.815876972085360697e-01 5.719314446940914065e-01 1.134353516976499415e-01
x_list = np.array(x_list)
y_list = np.array(y_list)
ax.plot(x_list, y_list, 'o-')
ax.axvline(51, linestyle=':', c='k',label='LZ design(liquid)')
ax.axvline(64, c='k',label='LZ design(gas equivalent)')
ax.set_xlabel('Average surface electric field on the wire (kV/cm)')
ax.set_ylabel('electron emission rate (Hz)')
ax.legend()
ax.grid('on')
plt.savefig(workdir+'Run2_result.png')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xx = 1./x_list[:]
yy = np.log(y_list/x_list**2)[:]
plt.plot(xx[2:], yy[2:], 'o-', label='data')
slope, intercept, r_value, p_value, std_err = stats.linregress(xx[2:],yy[2:])
xxx= np.linspace(xx[-1], xx[-3]*1.2, 100)
yyy = slope* xxx + intercept
plt.plot(xxx,yyy, label = 'linear regression fit')
workfunction=4.4
beta = -6.83e9*workfunction**(3/2.)/slope/1.e5 
ax.set_xlabel(r'$1/E$ $(kV/cm)^{-1}$')
ax.set_ylabel(r'$\ln(j/E^2)$ $(Hz) (kV/cm)^{-2}$')
ax.legend()
ax.grid('on')
plt.savefig(workdir+'Run2_result_rev.png')


print slope
print beta

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x_list = [8,10,12]
#y_list = [3.6, 2.9, 2.4]
y_list = [3.816, 2.992, 2.464]
x_list = np.array(x_list)
y_list = np.array(y_list)-.12
#erry_list = [.1,.1,.1]
erry_list1 = [.236,.164,.164]
erry_list2 = [.852,.652,.436]
ax.errorbar(x_list, y_list, yerr=[erry_list1,erry_list2], fmt = 'o', label='data')
y_list = [3.461, 2.696,  2.221,]
ax.plot(x_list, y_list, '-', label='sim: 3.3 bara, 295K')
ax.set_xlabel(r'$V_A-V_G$ (kV)')
ax.set_ylabel('Drift time (us)')
ax.legend()
ax.grid('on')
plt.savefig(workdir+'Run2_drifttime.png')