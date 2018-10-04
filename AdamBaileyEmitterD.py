# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:01:29 2018

@author: wei
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
x_list=[95,98]
y_list=[6.3,110]
x_list = np.array(x_list)
y_list = np.array(y_list)
xx = 1./x_list[:]
yy = np.log(y_list/x_list**2)[:]
plt.plot(xx[1:], yy[1:], 'o-', label='data')
slope, intercept, r_value, p_value, std_err = stats.linregress(xx[:],yy[:])
xxx= np.linspace(xx[-1], xx[0], 100)
yyy = slope* xxx + intercept
plt.plot(xxx,yyy, label = 'linear regression fit')
workfunction=4.4
beta = -6.83e9*workfunction**(3/2.)/slope/1.e5 