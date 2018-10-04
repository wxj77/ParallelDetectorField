# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:43:47 2017

@author: wei
"""

import matplotlib.ticker as tck
workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
import scipy.integrate as integ
import unit
import numpy as np

def ElectronCurrent(E, WorkFunction = 4.4, ifprint=False):
    if E>0:
        return 0.
    E = -E
     #eV
    Vtemp = E/4.5e3*100./1.e3
    A = -934
    B = -A*.01025 - 9.75
    return 1./unit.eV* np.exp(A/Vtemp+B)*Vtemp**2*1.e-9#1.e-6 m^2-> mm^2 1.e-9 nA->A

def ElectronCurrentAdderley(E, Beta=134, WorkFunction = 4.4, ifprint=False):
    #From P. Adderley, Evaluation of niobium as candidate electrode material for dc high voltage photoelectron guns, Table 2,3
    #DPP-SS2 Post-Kr Treat
    #ENorm = E*1.e3#1.e3 V/mm -> V/m
    #Beta = 316
    if E>0:
        return 0.
    E = -E
    WorkFunction = 4.4 #eV
    A= -6.53e9*WorkFunction**1.5/Beta
    B= 1.2e-22
    return 1./unit.eV* np.exp(A/E+B)*E**2
 
def ElectronCurrentBastaniNejad(E, Beta =134, WorkFunction = 4.4, ifprint=False):
	#From M. BastaniNejad, Improving the performance of stainless-steel DC high voltage photoelectron gun cathode electrodes via gas conditioning with helium or krypton, Table 2
	#316L#2 Pre-gas 
	#ENorm = E*1.e3#1.e3 V/mm -> V/m
	#Beta = 134
    if E>0:
        return 0.
    E = -E
    WorkFunction = 4.4 #eV
    Intercept = 2.5e-20
    A= -2.85e9*WorkFunction**1.5/Beta#-1.11e8#
#    	print "A",A,"Intercept",Intercept
    B= np.log10(1.54e-6*Beta**2*10**(4.52*WorkFunction**(-0.5))/WorkFunction)#-2.95#
    return 1./unit.eV* 10**(A/E+B)*E**2*1.#1.e-6 m^2-> mm^2