# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:09:49 2017

@author: wei
"""

#unit in this script is V, mm.
printless = False # will print more detail if set to True.
X = 0 #How much distance have you shifted the detector from liquid level = 0 if you want complete gas, put X=100000;
#workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
#sys.path.insert(0, "/media/wei/ACA8-1ECD1/SystemTest//XenonProperty/")
#sys.path.insert(0, "/media/wei/ACA8-1ECD3/SystemTest//XenonProperty/")
#sys.path.insert(0, workdir)
import unit
import CalculateField as cf
import numpy as np

############################################################
#LZ Baseline Current. 50kV
############################################################

#LengthUnit="mm", ForceUnit="N", StressUnit="MPa",
GridList=[]
TopPlate = cf.LZ_Grid(GridName = "Top Plate",WireDiameter = 1456.*unit.m, WirePitch = 0.*unit.m, GridType = "P", z_Location = (70.+8.+X)*unit.m, Tension = 0.,GridDiameter = 1465.*unit.m, MaterialMaxStress = 290.*unit.M)
#TopPlate.ElectricFieldUpInf = 0. # in V/mm
#TopPlate.ElectricFieldDownInf = .114e2  #in V/mm
#TopPlate.Print()
GridList.append(TopPlate)

AnodeGrid = cf.LZ_Grid(GridName = "Anode Grid",WireDiameter = 100.e-3*unit.m, WirePitch = 2.5*unit.m, GridType = "WW", z_Location = (8.+X)*unit.m, Tension = 2.5, GridDiameter = 1465.*unit.m, MaterialMaxStress = 290.*unit.M)
#AnodeGrid.ElectricFieldUpInf = .114e2 # in V/mm
#AnodeGrid.ElectricFieldDownInf = -10.2e2  #in V/mm
#AnodeGrid.Print()
GridList.append(AnodeGrid)

GateGrid = cf.LZ_Grid(GridName = "Gate Grid",WireDiameter = 75.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-5.+X)*unit.m, Tension = 2.5, GridDiameter = 1465.*unit.m, MaterialMaxStress = 290.*unit.M)
#GateGrid.ElectricFieldUpInf = -6.1e2 # in V/mm
#GateGrid.ElectricFieldDownInf = -.366e2  #in V/mm
#GateGrid.Print()
GridList.append(GateGrid)

CathodeGrid = cf.LZ_Grid(GridName = "Cathode Grid",WireDiameter = 100.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-5.-1456.+X)*unit.m, Tension = 2.5, GridDiameter = 1465.*unit.m, MaterialMaxStress = 290.*unit.M)
#CathodeGrid.ElectricFieldUpInf = -6.1e2 # in V/mm
#CathodeGrid.ElectricFieldDownInf = -.366e2  #in V/mm
#CathodeGrid.Print()
GridList.append(CathodeGrid)

BottomGrid = cf.LZ_Grid(GridName = "Bottom Grid",WireDiameter = 75.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-5.-1456.-137.5+X)*unit.m, Tension = 2.5, GridDiameter = 1465.*unit.m, MaterialMaxStress = 290.*unit.M)
#BottomGrid.ElectricFieldUpInf = -.366e2 # in V/mm
#BottomGrid.ElectricFieldDownInf = 2.90e2  #in V/mm
#BottomGrid.Print()
GridList.append(BottomGrid)

BottomPlate = cf.LZ_Grid(GridName = "Bottom Plate",WireDiameter = 1456.*unit.m, WirePitch = 0.*unit.m, GridType = "P", z_Location = (-5.-1456.-137.5-10.+X)*unit.m, Tension = 0., GridDiameter = 1465.*unit.m, MaterialMaxStress = 290.*unit.M)
#BottomPlate.ElectricFieldUpInf = 2.90e2 # in V/mm
#BottomPlate.ElectricFieldDownInf = .25e2  #in V/mm
#BottomPlate.Print()
GridList.append(BottomPlate)

print "############################################################"
print "############################################################"
print "############################################################"
print "############################################################"
print "LZ Baseline Current. 50 kV Cathode. "

LZ= cf.LZ_detector(GridList)
#VList=[-0.e3,5.75e3,-5.75e3,-50e3,-1.5e3,-0.e3,]
VList=[-1.5e3,5.75e3,-5.75e3,-50e3,-1.5e3,-1.5e3,]

LZ.UpdateVoltage(VList)
LZ.Print(printless)
print "Voltage on ","20","mm is", LZ.GetVoltageInZLocation(20.*unit.m)
print "Voltage on "," 15","mm is", LZ.GetVoltageInZLocation(15.*unit.m)
print "Voltage on "," 0","mm is", LZ.GetVoltageInZLocation(0)
print "Voltage on ","-15","mm is", LZ.GetVoltageInZLocation(-15.*unit.m)
print "Voltage on ","-20","mm is", LZ.GetVoltageInZLocation(-20.*unit.m)
print "Voltage on ","-25","mm is", LZ.GetVoltageInZLocation(-25.*unit.m)
print "Voltage on ","-30","mm is", LZ.GetVoltageInZLocation(-30.*unit.m)
print "Voltage on ","-35","mm is", LZ.GetVoltageInZLocation(-35.*unit.m)
print "############################################################"
print "############################################################"
print "############################################################"
print "############################################################"




drift_voltage_list=[]
for a in range(7):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    LZ.UpdateVoltage(VList)
    drift_voltage_list.append(LZ.GridList[1].ElectricFieldDownInf/1.e5)
    print LZ.GridList[1].ElectricFieldDownInf/1.e5
    print LZ.GridList[2].SurfaceFieldNaive()


drift_voltage_list=[]
for a in range(7):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    LZ.UpdateVoltage(VList)
    drift_voltage_list.append(LZ.GridList[1].ElectricFieldDownInf/1.e5)
    print LZ.GridList[1].ElectricFieldDownInf/1.e5
    print LZ.GridList[2].SurfaceFieldNaive()

drift_time= [ 3.6 , 2.9, 2.4]

ss=""
surface_voltage_list=[]
for a in np.arange(0,8.5,0.5):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    LZ.UpdateVoltage(VList)
    surface_voltage_list.append(LZ.GridList[1].SurfaceFieldNaive()/1.e5)
    ss=ss+ '%.2f,'%((LZ.GridList[1].SurfaceFieldNaive()[0]/1.e5))   
    print '%.2f,'%((LZ.GridList[1].SurfaceFieldNaive()[0]/1.e5))

print ss
ss=""
surface_voltage_list=[]
for a in np.arange(0,8.5,0.5):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    LZ.UpdateVoltage(VList)
    surface_voltage_list.append(LZ.GridList[2].SurfaceFieldNaive()/1.e5)
    ss=ss+ '%.2f,'%(-(LZ.GridList[2].SurfaceFieldNaive()[0]/1.e5))  
    print '%.2f,'%(-(LZ.GridList[2].SurfaceFieldNaive()[0]/1.e5))

print ss

    
