# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:37:42 2017

@author: wei
"""

workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
#from ComsolSurfaceFieldEmissionRate import *
from ElectronCurrentFunctions import *

import numpy as np
import matplotlib.pyplot as plt
import calendar
import scipy.stats
#import cPickle as cp
import matplotlib.colors as colors
import math
import unit
from SystemTest_Baseline_Detector import *

SYS_Gas.GridList[2].GridType
SYS_Gas.GridList[2].GridName
SYS_Gas.GridList[2].ElectricFieldUpInf

NumberOfSteps = 101
RampVoltageTopShieldList = [0]*NumberOfSteps
RampVoltageAnodeList = np.linspace(0000,8000, num = NumberOfSteps,endpoint=True)
RampVoltageGateList = [-4000]* NumberOfSteps
RampVoltageCathodeList = [0]*NumberOfSteps
RampVoltageBottomList = [0]* NumberOfSteps
RampVoltageBotShieldList = [0]*NumberOfSteps

#2 is gate grid.
gridnum=2
EBotList_Gas=[]
EBotTopDifList_Gas=[]
ERatioList_Gas = []
for VList in zip(RampVoltageTopShieldList, RampVoltageAnodeList, RampVoltageGateList, RampVoltageCathodeList, RampVoltageBottomList, RampVoltageBotShieldList):
    print "VList =", VList    
    SYS_Gas.UpdateVoltage(VList)
    print "EFieldUpInf on", SYS_Gas.GridList[gridnum].GridName, SYS_Gas.GridList[gridnum].GridType, "is", SYS_Gas.GridList[gridnum].ElectricFieldUpInf, "V/m"
    print "EFieldDownInf on", SYS_Gas.GridList[gridnum].GridName, SYS_Gas.GridList[gridnum].GridType, "is", SYS_Gas.GridList[gridnum].ElectricFieldDownInf, "V/m"
    print SYS_Gas.GridList[gridnum].ElectricFieldUpInf/SYS_Gas.GridList[gridnum].ElectricFieldDownInf
    EBotList_Gas.append(SYS_Gas.GridList[gridnum].ElectricFieldDownInf)
    EBotTopDifList_Gas.append(SYS_Gas.GridList[gridnum].ElectricFieldDownInf- SYS_Gas.GridList[gridnum].ElectricFieldUpInf)
    ERatioList_Gas.append(SYS_Gas.GridList[gridnum].ElectricFieldUpInf/SYS_Gas.GridList[gridnum].ElectricFieldDownInf)
    
RatePerAreaList_Gas = []
RatePerAreaListAdderley_Gas = []
RatePerAreaListBastaniNejad_Gas = [] 
for ii in range(len(ERatioList_Gas)):  
    #fillpoints = np.array([X,Y,np.ones_like(X)*ERatioList[ii]]).T
    #valuepoints = interpolate.LinearNDInterpolator(EFieldPoints, EFieldValues)(fillpoints)
    array_xx = np.linspace(0,5e-3,201,endpoint= True)
    array_xx2 = 0.5* (array_xx[1:]+array_xx[:-1])-2.5e-3
    EFieldFitPoly8= np.array([  1.21808017e+01,  -1.28471352e+05,  -4.22463723e+11, 1.41613046e+17,  -1.73500001e+22])

    valuepoints = EFieldFitPoly8[0] + EFieldFitPoly8[1] *array_xx2**2 + EFieldFitPoly8[2] * array_xx2**4 +EFieldFitPoly8[3] *array_xx2**6+EFieldFitPoly8[4] *array_xx2**8
    values= np.vectorize(ElectronCurrentAdderley)(-valuepoints * EBotTopDifList_Gas[ii])        
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())  
    RatePerAreaListAdderley_Gas.append(value)
    
    values= np.vectorize(ElectronCurrentBastaniNejad)(-valuepoints * EBotTopDifList_Gas[ii])    
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())    
    RatePerAreaListBastaniNejad_Gas.append(value)

    values= np.vectorize(ElectronCurrent)(-valuepoints * EBotTopDifList_Gas[ii])   
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())  
    RatePerAreaList_Gas.append(value)


#2 is gate grid.
gridnum=2
EBotList_Liq=[]
EBotTopDifList_Liq=[]
ERatioList_Liq = []
for VList in zip(RampVoltageTopShieldList, RampVoltageAnodeList, RampVoltageGateList, RampVoltageCathodeList, RampVoltageBottomList, RampVoltageBotShieldList):
    print "VList =", VList    
    SYS_Liq.UpdateVoltage(VList)
    print "EFieldUpInf on", SYS_Liq.GridList[gridnum].GridName, SYS_Liq.GridList[gridnum].GridType, "is", SYS_Liq.GridList[gridnum].ElectricFieldUpInf, "V/m"
    print "EFieldDownInf on", SYS_Liq.GridList[gridnum].GridName, SYS_Liq.GridList[gridnum].GridType, "is", SYS_Liq.GridList[gridnum].ElectricFieldDownInf, "V/m"
    print SYS_Liq.GridList[gridnum].ElectricFieldUpInf/SYS_Liq.GridList[gridnum].ElectricFieldDownInf
    EBotList_Liq.append(SYS_Liq.GridList[gridnum].ElectricFieldDownInf)
    EBotTopDifList_Liq.append(SYS_Liq.GridList[gridnum].ElectricFieldDownInf- SYS_Liq.GridList[gridnum].ElectricFieldUpInf)
    ERatioList_Liq.append(SYS_Liq.GridList[gridnum].ElectricFieldUpInf/SYS_Liq.GridList[gridnum].ElectricFieldDownInf)
    
RatePerAreaList_Liq = []
RatePerAreaListAdderley_Liq = []
RatePerAreaListBastaniNejad_Liq = [] 
for ii in range(len(ERatioList_Liq)):  
    #fillpoints = np.array([X,Y,np.ones_like(X)*ERatioList[ii]]).T
    #valuepoints = interpolate.LinearNDInterpolator(EFieldPoints, EFieldValues)(fillpoints)
    array_xx = np.linspace(0,5e-3,201,endpoint= True)
    array_xx2 = 0.5* (array_xx[1:]+array_xx[:-1])-2.5e-3
    #EFieldFitPoly
    valuepoints = EFieldFitPoly8[0] + EFieldFitPoly8[1] *array_xx2**2 + EFieldFitPoly8[2] * array_xx2**4 +EFieldFitPoly8[3] *array_xx2**6+EFieldFitPoly8[4] *array_xx2**8
    values= np.vectorize(ElectronCurrentAdderley)(-valuepoints * EBotTopDifList_Liq[ii], WorkFunction=3.8)        
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())  
    RatePerAreaListAdderley_Liq.append(value)
    
    values= np.vectorize(ElectronCurrentBastaniNejad)(-valuepoints * EBotTopDifList_Liq[ii], WorkFunction=3.8)    
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())    
    RatePerAreaListBastaniNejad_Liq.append(value)

    values= np.vectorize(ElectronCurrent)(-valuepoints * EBotTopDifList_Liq[ii], WorkFunction=3.8)   
    value = np.sum(values[np.isfinite(values)])/len(values.flatten())  
    RatePerAreaList_Liq.append(value)
   
fignum=100
# Plot start
scale = SYS_Gas.GridList[gridnum].WireSurface()
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
#ax1.plot(RampVoltageAnodeList/unit.k,np.array(RatePerAreaList)*scale, "ro-", label = "method 1")
ax1.plot(RampVoltageAnodeList/unit.k,np.array(RatePerAreaListAdderley_Gas)*scale, "bo-", label = "Adderley, Gas")
ax1.plot(RampVoltageAnodeList/unit.k,np.array(RatePerAreaListBastaniNejad_Gas)*scale, "go-", label = "BastaniNejad, Gas")

ax1.plot(RampVoltageAnodeList/unit.k,np.array(RatePerAreaListAdderley_Liq)*scale, "b>-", label = "Adderley, Liquid")
ax1.plot(RampVoltageAnodeList/unit.k,np.array(RatePerAreaListBastaniNejad_Liq)*scale, "g>-", label = "BastaniNejad, Liquid")
#ax1.set_yscale('log')
ax1.set_xlabel("Anode Voltage (kV)")
#ax1.set_ylabel(r"$s^{-1}m^{-2}$")
ax1.set_ylabel(r"$s^{-1}$")
ax1.set_xlim(3,8)
ax1.set_ylim(0,1.e-1)

ax1.set_title("Rate in system test: \n V_TopShield =0 kV, V_Gate= -4 kV, V_Cat= +4 kV, \nV_Bot =0 kV, V_BotShield =0 kV")

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

#end of 2 is gate grid.