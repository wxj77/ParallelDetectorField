# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:11:57 2017

@author: wei
"""
#unit in this script is V, mm.
#to put detector in ga
X=0000

printless = False
#printless = True
workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, "/media/wei/ACA8-1ECD1/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
import unit
import CalculateField as cf
import numpy as np
############################################################
#System Test Current.
############################################################

#LengthUnit="mm", ForceUnit="N", StressUnit="MPa",
GridList=[]
TopPlate = cf.LZ_Grid(GridName = "Top Plate",WireDiameter = 1465.*unit.m, WirePitch = 0.*unit.m, GridType = "P", z_Location = (57.+8.125+X)*unit.m, Tension = 0.,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#TopPlate.ElectricFieldUpInf = 0. # in V/mm
#TopPlate.ElectricFieldDownInf = .114e2  #in V/mm
#TopPlate.Print()
GridList.append(TopPlate)

AnodeGrid = cf.LZ_Grid(GridName = "Anode Grid",WireDiameter = 100.e-3*unit.m, WirePitch = 2.5*unit.m, GridType = "WW", z_Location = (8.125+X)*unit.m, Tension = 2.5,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#AnodeGrid.ElectricFieldUpInf = .114e2 # in V/mm
#AnodeGrid.ElectricFieldDownInf = -10.2e2  #in V/mm
#AnodeGrid.Print()
GridList.append(AnodeGrid)

GateGrid = cf.LZ_Grid(GridName = "Gate Grid",WireDiameter = 68.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-4.875+X)*unit.m, Tension = 3.3,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#GateGrid.ElectricFieldUpInf = -6.1e2 # in V/mm
#GateGrid.ElectricFieldDownInf = -.366e2  #in V/mm
#GateGrid.Print()
GridList.append(GateGrid)

CathodeGrid = cf.LZ_Grid(GridName = "Cathode Grid",WireDiameter = 100.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-4.875-512.+X)*unit.m, Tension = 5.0,GridDiameter = 146. *unit.m, MaterialMaxStress = 290.*unit.M)
#CathodeGrid.ElectricFieldUpInf = -6.1e2 # in V/mm
#CathodeGrid.ElectricFieldDownInf = -.366e2  #in V/mm
#CathodeGrid.Print()
GridList.append(CathodeGrid)

BottomGrid = cf.LZ_Grid(GridName = "Bottom Grid",WireDiameter = 75.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-4.875-512.-88.+X)*unit.m, Tension = 2.5, GridDiameter = 146. *unit.m, MaterialMaxStress = 290.*unit.M)
#BottomGrid.ElectricFieldUpInf = -.366e2 # in V/mm
#BottomGrid.ElectricFieldDownInf = 2.90e2  #in V/mm
#BottomGrid.Print()
GridList.append(BottomGrid)

BottomPlate = cf.LZ_Grid(GridName = "Bottom Plate",WireDiameter = 1465.*unit.m, WirePitch = 0.*unit.m, GridType = "P", z_Location = (-4.875-512.-88.-70.+X)*unit.m, Tension = 0.,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#BottomPlate.ElectricFieldUpInf = 2.90e2 # in V/mm
#BottomPlate.ElectricFieldDownInf = .25e2  #in V/mm
#BottomPlate.Print()
GridList.append(BottomPlate)

print "############################################################"
print "############################################################"
print "############################################################"
print "############################################################"
print "System Test Current. 50 kV Cathode. "

SYS_Gas= cf.LZ_detector(GridList)
VList=[-1.5e3,4e3,-4e3,0,-1.5e3,-1.5e3,]
SYS_Gas.UpdateVoltage(VList)
SYS_Gas.Print(printless)
print "Voltage on "," 15","mm is", SYS_Gas.GetVoltageInZLocation(15.*unit.m)
print "Voltage on ","-15","mm is", SYS_Gas.GetVoltageInZLocation(-15.*unit.m)

print "############################################################"
print "############################################################"
print "############################################################"
print "############################################################"



X=100000#//set to be liquid

printless = False
workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
import unit
import CalculateField as cf
import numpy as np
############################################################
#System Test Current.
############################################################

#LengthUnit="mm", ForceUnit="N", StressUnit="MPa",
GridList=[]
TopPlate = cf.LZ_Grid(GridName = "Top Plate",WireDiameter = 1465.*unit.m, WirePitch = 0.*unit.m, GridType = "P", z_Location = (57.+8.125+X)*unit.m, Tension = 0.,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#TopPlate.ElectricFieldUpInf = 0. # in V/mm
#TopPlate.ElectricFieldDownInf = .114e2  #in V/mm
#TopPlate.Print()
GridList.append(TopPlate)

AnodeGrid = cf.LZ_Grid(GridName = "Anode Grid",WireDiameter = 100.e-3*unit.m, WirePitch = 2.5*unit.m, GridType = "WW", z_Location = (8.125+X)*unit.m, Tension = 2.5,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#AnodeGrid.ElectricFieldUpInf = .114e2 # in V/mm
#AnodeGrid.ElectricFieldDownInf = -10.2e2  #in V/mm
#AnodeGrid.Print()
GridList.append(AnodeGrid)

GateGrid = cf.LZ_Grid(GridName = "Gate Grid",WireDiameter = 75.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-4.875+X)*unit.m, Tension = 3.3,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#GateGrid.ElectricFieldUpInf = -6.1e2 # in V/mm
#GateGrid.ElectricFieldDownInf = -.366e2  #in V/mm
#GateGrid.Print()
GridList.append(GateGrid)

CathodeGrid = cf.LZ_Grid(GridName = "Cathode Grid",WireDiameter = 100.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-4.875-512.+X)*unit.m, Tension = 5.0,GridDiameter = 146. *unit.m, MaterialMaxStress = 290.*unit.M)
#CathodeGrid.ElectricFieldUpInf = -6.1e2 # in V/mm
#CathodeGrid.ElectricFieldDownInf = -.366e2  #in V/mm
#CathodeGrid.Print()
GridList.append(CathodeGrid)

BottomGrid = cf.LZ_Grid(GridName = "Bottom Grid",WireDiameter = 75.e-3*unit.m, WirePitch = 5.*unit.m, GridType = "WW", z_Location = (-4.875-512.-88.+X)*unit.m, Tension = 2.5, GridDiameter = 146. *unit.m, MaterialMaxStress = 290.*unit.M)
#BottomGrid.ElectricFieldUpInf = -.366e2 # in V/mm
#BottomGrid.ElectricFieldDownInf = 2.90e2  #in V/mm
#BottomGrid.Print()
GridList.append(BottomGrid)

BottomPlate = cf.LZ_Grid(GridName = "Bottom Plate",WireDiameter = 1465.*unit.m, WirePitch = 0.*unit.m, GridType = "P", z_Location = (-4.875-512.-88.-70.+X)*unit.m, Tension = 0.,GridDiameter = 146.*unit.m , MaterialMaxStress = 290.*unit.M)
#BottomPlate.ElectricFieldUpInf = 2.90e2 # in V/mm
#BottomPlate.ElectricFieldDownInf = .25e2  #in V/mm
#BottomPlate.Print()
GridList.append(BottomPlate)

print "############################################################"
print "############################################################"
print "############################################################"
print "############################################################"
print "System Test Current. 50 kV Cathode. "

SYS_Liq= cf.LZ_detector(GridList)
VList=[-1.5e3,5.75e3,-5.75e3,0,-1.5e3,-1.5e3,]
SYS_Liq.UpdateVoltage(VList)
SYS_Liq.Print(printless)
print "Voltage on "," 15","mm is", SYS_Liq.GetVoltageInZLocation(15.*unit.m)
print "Voltage on ","-15","mm is", SYS_Liq.GetVoltageInZLocation(-15.*unit.m)

print "############################################################"
print "############################################################"
print "############################################################"
print "############################################################"




drift_voltage_list=[]
for a in range(7):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    SYS_Gas.UpdateVoltage(VList)
    drift_voltage_list.append(SYS_Gas.GridList[1].ElectricFieldDownInf/1.e5)
    print SYS_Gas.GridList[1].ElectricFieldDownInf/1.e5
    print SYS_Gas.GridList[2].SurfaceFieldNaive()


drift_voltage_list=[]
for a in range(7):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    SYS_Liq.UpdateVoltage(VList)
    drift_voltage_list.append(SYS_Liq.GridList[1].ElectricFieldDownInf/1.e5)
    print SYS_Liq.GridList[1].ElectricFieldDownInf/1.e5
    print SYS_Liq.GridList[2].SurfaceFieldNaive()

drift_time= [ 3.6 , 2.9, 2.4]

ss=""
surface_voltage_list=[]
for a in np.arange(0,8.5,0.5):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    SYS_Liq.UpdateVoltage(VList)
    surface_voltage_list.append(SYS_Liq.GridList[1].SurfaceFieldNaive()/1.e5)
    ss=ss+ '%.2f,'%((SYS_Liq.GridList[1].SurfaceFieldNaive()[0]/1.e5))   
    print '%.2f,'%((SYS_Liq.GridList[1].SurfaceFieldNaive()[0]/1.e5))

print ss
ss=""
surface_voltage_list=[]
for a in np.arange(0,8.5,0.5):
    VList=[-1.5e3,a*1e3,-a*1.e3,0,-1.5e3,-1.5e3,]
    SYS_Liq.UpdateVoltage(VList)
    surface_voltage_list.append(SYS_Liq.GridList[2].SurfaceFieldNaive()/1.e5)
    ss=ss+ '%.2f,'%(-(SYS_Liq.GridList[2].SurfaceFieldNaive()[0]/1.e5))  
    print '%.2f,'%(-(SYS_Liq.GridList[2].SurfaceFieldNaive()[0]/1.e5))

print ss

    