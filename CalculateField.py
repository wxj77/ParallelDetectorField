# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:05:02 2017

@author: wei
"""
#workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
#sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
#sys.path.insert(0, workdir)
import unit

import sys
#import ast
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.interpolate as interp
import scipy.integrate as integrate
import scipy.io as sio
import scipy.optimize as opt

from mpl_toolkits.mplot3d import Axes3D

#define a class for grid calculation

DielectricConstant0 = 8.85e-12
printless = True
if (len(sys.argv)>1):
    if (sys.argv[1]=="False") or (sys.argv[1] == "0"):
        printless = False
    elif (sys.argv[1]=="True") or (sys.argv[1] == "1"):
        printless = True
print "print less = ", printless

class LZ_Grid:
    def __init__(self, GridName, WireDiameter, WirePitch, GridType, z_Location, Tension, GridDiameter=1465. *unit.m, DielectricConstant=1., z0AtLiquidGasInterface= True ,MaterialMaxStress=290.*unit.M, LengthUnit="m", ForceUnit="N", StressUnit="Pa",LiquidLevel=0):
        self.GridName = GridName
        self.LengthUnit = LengthUnit
        self.ForceUnit = ForceUnit
        self.WireDiameter = WireDiameter
        self.WirePitch = WirePitch
        self.z_Location = z_Location
        self.Tension = Tension
        self.GridType = GridType
        self.MaterialMaxStress = MaterialMaxStress
        self.GridDiameter = GridDiameter 
        self.ElectricFieldUpInf=0.
        self.ElectricFieldDownInf=0.
        self.Voltage0 =  0.
        self.Voltage =  0.
        self.LiquidLevel=0
        if z0AtLiquidGasInterface:
            # 0 is default liquid level            
            if (z_Location > LiquidLevel):
                self.DielectricConstant = 1.
            else:
                self.DielectricConstant = 1.96
        elif (DielectricConstant >LiquidLevel):
            self.DielectricConstant = DielectricConstant
        else:
            print "Dielectric Constant is not valid. Re initialize the grid."
            #break
        if (GridType == "Plate") or  (GridType == "P"):
            self.GridType = "Plate"            
            self.SurfaceFieldFactor = 1. 
        elif (GridType == "Parallel Wire") or  (GridType == "PW"):
            self.GridType = "Parallel Wire"            
            self.SurfaceFieldFactor = 1. 
        elif (GridType == "Mesh Wire") or  (GridType == "MW"):
            self.GridType = "Mesh Wire"
            self.SurfaceFieldFactor = 1. 
        elif (GridType == "Woven Wire") or  (GridType == "WW"):
            self.GridType = "Woven Wire"
            self.SurfaceFieldFactor = 1.             
        else:
            print "Grid Type is not valid. Re initialize the grid."
            #break 
    def GridFactor(self):
        if (self.GridType == "Plate") or  (self.GridType == "P"):
            return 0.
        elif (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return 1./(2.*np.pi)*np.log(self.WirePitch/(np.pi*self.WireDiameter))
        elif (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            return 1./2./(2.*np.pi)*np.log(self.WirePitch/2./(np.pi*self.WireDiameter))
        elif (self.GridType == "Woven Wire") or  (self.GridType == "WW"):
            return 0.5247*1./(2.*np.pi)*np.log(0.5247*self.WirePitch/(np.pi*self.WireDiameter*0.7488))                
        else:
            print "Grid Type is not valid. Re initialize the grid."
            #break 

    def Transparency(self):
        if (self.GridType == "Plate") or  (self.GridType == "P"):
            return 0.
        elif (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return (self.WirePitch-self.WireDiameter)/(self.WirePitch)
        elif (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            return ( (self.WirePitch-self.WireDiameter)/(self.WirePitch) )**2
        elif (self.GridType == "Woven Wire") or  (self.GridType == "WW"):
            return ( (self.WirePitch-self.WireDiameter)/(self.WirePitch) )**2            
        else:
            print "Grid Type is not valid. Re initialize the grid."
            #break
    def WireSurface(self):
        if (self.GridType == "Plate") or  (self.GridType == "P"):
            return 0.
        Num=int(np.floor(self.GridDiameter/self.WirePitch/2.))         
        Sum=0
        for ii in range(-Num,Num+1):
            Sum=Sum+np.sqrt(self.GridDiameter**2-(2.*ii*self.WirePitch)**2)
        Sum = Sum * np.pi * self.WireDiameter
        if (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return Sum
        elif (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            return Sum*2.
        elif (self.GridType == "Woven Wire") or  (self.GridType == "WW"):
            return Sum*2.            
        else:
            print "Grid Type is not valid. Re initialize the grid."
            #break
        

    def UnitLengthForceNaive(self): 
        if (self.GridType == "Woven Wire") or  (self.GridType == "WW")\
        or (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            return 1./2. * DielectricConstant0 * self.DielectricConstant\
                * (self.ElectricFieldDownInf**2 - self.ElectricFieldUpInf**2) * (1./2. * self.WirePitch**2) / self.WirePitch 
        if (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return 1./2. * DielectricConstant0 * self.DielectricConstant\
                * (self.ElectricFieldDownInf**2 - self.ElectricFieldUpInf**2) * self.WirePitch 

    def UnitLengthChargeNaive(self): 
        if (self.GridType == "Woven Wire") or  (self.GridType == "WW")\
        or (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            return 1. * DielectricConstant0 * self.DielectricConstant \
                * (-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * (1./2. * self.WirePitch**2) / self.WirePitch 
        if (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return 1. * DielectricConstant0 * self.DielectricConstant\
                * (-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * self.WirePitch 

    def SurfaceFieldNaive(self):         
        if (self.GridType == "Plate") or  (self.GridType == "P"):
            return np.array([(-self.ElectricFieldDownInf + self.ElectricFieldUpInf) ,\
                    (-self.ElectricFieldDownInf ) ,\
                    (self.ElectricFieldUpInf) ,])

        if (self.GridType == "Woven Wire") or  (self.GridType == "WW")\
        or (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            #return self.UnitLengthChargeNaive()/(self.DielectricConstant *DielectricConstant0)/(np.pi* self.WireDiameter)
            return np.array([(-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * (1./2. * self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter),\
                    (-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * (1./2. * self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter)\
                        +0.5* (self.ElectricFieldDownInf + self.ElectricFieldUpInf),\
                    (-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * (1./2. * self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter)\
                        -0.5* (self.ElectricFieldDownInf + self.ElectricFieldUpInf),\
                    (-self.ElectricFieldDownInf ) * (1./2. * self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter/2.),\
                    (self.ElectricFieldUpInf) * (1./2. * self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter/2.),])
        if (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return np.array([(-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * (self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter),\
                    (-self.ElectricFieldDownInf + self.ElectricFieldUpInf) * (self.WirePitch**2) / (self.WirePitch* np.pi* self.WireDiameter)\
                        +0.5* (self.ElectricFieldDownInf + self.ElectricFieldUpInf)])

    def DeflectionNaive(self): 
        if (self.GridType == "Woven Wire") or  (self.GridType == "WW")\
        or (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
            return  self.UnitLengthForceNaive()*self.GridDiameter**2/(8.*self.Tension)
        if (self.GridType == "Parallel Wire") or  (self.GridType == "PW"):
            return self.UnitLengthForceNaive()*self.GridDiameter**2/(8.*self.Tension) 


    def GetVoltageFromField(self):
        self.Voltage = self.Voltage0 + (self.ElectricFieldUpInf-self.ElectricFieldDownInf)*self.GridFactor()*self.WirePitch

    def Print(self,PrintLess=True):
        print "############################################################"
        print "Print Less = ", PrintLess
        if (PrintLess == 0):
            print "Grid Name: ", self.GridName
            print "Grid Type: ",self.GridType
            print "Grid Location: ", self.z_Location," ",self.LengthUnit
            print "Wire Diameter: ", self.WireDiameter, " ", self.LengthUnit
            print "Wire Pitch: ", self.WirePitch, " ", self.LengthUnit
            print "Wire Surface", self.WireSurface(), " ", self.LengthUnit,"^2"

            print "Dielectric Constant: ", self.DielectricConstant
            print "Transparency: ", self.Transparency()

            print "Tension: ", self.Tension," ", self.ForceUnit
            print "\t", self.Tension/(self.MaterialMaxStress * np.pi * self.WireDiameter**2 /4. ) *100., "% of Maximum Stress: ", self.MaterialMaxStress, "Pa"
        

            if (self.GridType == "Woven Wire") or  (self.GridType == "WW")\
            or (self.GridType == "Mesh Wire") or  (self.GridType == "MW"):
                print "Unit Length Force Naive: ", self.UnitLengthForceNaive()," N/m" 
                print "Unit Length Charge Naive: ", self.UnitLengthChargeNaive()," C/m" 
                print "Surface Field Naive: ", self.SurfaceFieldNaive()/unit.k*unit.c," kV/cm" 
                print "Deflection Naive: ", self.DeflectionNaive(), "m"
            print "Grid Factor", self.GridFactor()
            print "Grid Factor Times Pitch", self.GridFactor()*self.WirePitch, self.LengthUnit
            #print "Surface Field Factor", self.SurfaceFieldFactor()
        
            print "Grid Voltage: ", self.Voltage/1.e3, "kV"
            print "Grid Equivalent Voltage : ", self.Voltage0/1.e3, "kV"
            print "Grid Electric Field in Positive Inf: ", self.ElectricFieldUpInf/unit.k*unit.c, "kV/cm"
            print "Grid Electric Field in Negative Inf: ", self.ElectricFieldDownInf/unit.k*unit.c, "kV/cm"
            print "############################################################"
            return 1
        else:
            print "Grid Name: ", self.GridName
            print "Grid Voltage: ", self.Voltage/1.e3, "kV"
            print "Grid Equivalent Voltage : ", self.Voltage0/1.e3, "kV"
            print "Grid Electric Field in Positive Inf: ", self.ElectricFieldUpInf/unit.k*unit.c, "kV/cm"
            print "Grid Electric Field in Negative Inf: ", self.ElectricFieldDownInf/unit.k*unit.c, "kV/cm"
        #    "############################################################"
            return 1
 
class LZ_detector:
    def __init__(self,GridListArgv):
        self.GridList=[]
        for arg in GridListArgv:
            self.GridList.append(arg)
        # Matrix is (Voltage0, E0up, E0down, Voltage1, E1up, E1down,...)
        self.CoffMatrixA = np.zeros([3*len(self.GridList),3*len(self.GridList),])
        self.CoffMatrixB = np.zeros([3*len(self.GridList),1,])


        #E top Inf = 0
        self.CoffMatrixA[0][0*3+1] = 1
        #E Bot Inf = 0
        self.CoffMatrixA[1][len(self.GridList)*3-1] = 1

        #E in different section is continuous on the boundary.
        for i in range(len(self.GridList)-1):
            self.CoffMatrixA[i+2][3*i+2]=self.GridList[i].DielectricConstant
            self.CoffMatrixA[i+2][3*i+4]=-self.GridList[i+1].DielectricConstant

        #E in different section is decided by Voltage0.
        for i in range(len(self.GridList)-1):
            self.CoffMatrixA[i+len(self.GridList)+1][3*i]=-1
            self.CoffMatrixA[i+len(self.GridList)+1][3*i+3]=1
            if (self.GridList[i].DielectricConstant == self.GridList[i+1].DielectricConstant):
                self.CoffMatrixA[i+len(self.GridList)+1][3*i+2]=-(self.GridList[i].z_Location-self.GridList[i+1].z_Location)
            else:
                self.CoffMatrixA[i+len(self.GridList)+1][3*i+2]=-(self.GridList[i].z_Location-0)
                self.CoffMatrixA[i+len(self.GridList)+1][3*i+4]=-(0-self.GridList[i+1].z_Location)

        #Voltage0 is related to Voltage by GridFactor and E grid up Inf, E grid bottom Inf        
        for i in range(len(self.GridList)):
            self.CoffMatrixA[i+2*len(self.GridList)][3*i]=1
            self.CoffMatrixA[i+2*len(self.GridList)][3*i+1]= self.GridList[i].GridFactor()*self.GridList[i].WirePitch    
            self.CoffMatrixA[i+2*len(self.GridList)][3*i+2]=    -self.GridList[i].GridFactor()*self.GridList[i].WirePitch
            self.CoffMatrixB[i+2*len(self.GridList)][0]=self.GridList[i].Voltage

    def UpdateDetector(self):
        self.CoffMatrixA = np.zeros([3*len(self.GridList),3*len(self.GridList),])
        self.CoffMatrixB = np.zeros([3*len(self.GridList),1,])


        #E top Inf = 0
        self.CoffMatrixA[0][0*3+1] = 1
        #E Bot Inf = 0
        self.CoffMatrixA[1][len(self.GridList)*3-1] = 1

        #E in different section is continuous on the boundary.
        for i in range(len(self.GridList)-1):
            self.CoffMatrixA[i+2][3*i+2]=self.GridList[i].DielectricConstant
            self.CoffMatrixA[i+2][3*i+4]=-self.GridList[i+1].DielectricConstant

        #E in different section is decided by Voltage0.
        for i in range(len(self.GridList)-1):
            self.CoffMatrixA[i+len(self.GridList)+1][3*i]=-1
            self.CoffMatrixA[i+len(self.GridList)+1][3*i+3]=1
            if (self.GridList[i].DielectricConstant == self.GridList[i+1].DielectricConstant):
                self.CoffMatrixA[i+len(self.GridList)+1][3*i+2]=-(self.GridList[i].z_Location-self.GridList[i+1].z_Location)
            else:
                self.CoffMatrixA[i+len(self.GridList)+1][3*i+2]=-(self.GridList[i].z_Location-0)
                self.CoffMatrixA[i+len(self.GridList)+1][3*i+4]=-(0-self.GridList[i+1].z_Location)

        #Voltage0 is related to Voltage by GridFactor and E grid up Inf, E grid bottom Inf        
        for i in range(len(self.GridList)):
            self.CoffMatrixA[i+2*len(self.GridList)][3*i]=1
            self.CoffMatrixA[i+2*len(self.GridList)][3*i+1]= self.GridList[i].GridFactor()*self.GridList[i].WirePitch    
            self.CoffMatrixA[i+2*len(self.GridList)][3*i+2]=    -self.GridList[i].GridFactor()*self.GridList[i].WirePitch
            self.CoffMatrixB[i+2*len(self.GridList)][0]=self.GridList[i].Voltage
        self.CalculateField()
        

    def UpdateVoltage(self,VList):
        if (len(VList)==len(self.GridList)):
            for i in range(len(self.GridList)):
                self.GridList[i].Voltage = VList[i]
                self.CoffMatrixB[i+2*len(self.GridList)][0]=self.GridList[i].Voltage
            self.CalculateField()
        else:
            print "Num of V is not equal to Num of Grids."
            return 0
    def CalculateField(self,):    
        x = np.linalg.solve(self.CoffMatrixA, self.CoffMatrixB)
        #print "A= ",CoffMatrixA
        #print "B= ",CoffMatrixB
        #print "x= ",x
        for i in range(len(self.GridList)):
            self.GridList[i].Voltage0 = x[3*i][0]
            self.GridList[i].ElectricFieldUpInf  = x[3*i+1][0]
            self.GridList[i].ElectricFieldDownInf  = x[3*i+2][0]


    def GetVoltageInZLocation(self, z, LengthUnit="mm"):
        for ii in range(len(self.GridList)):
            if (z >= self.GridList[0].z_Location):
                return self.GridList[0].Voltage0-self.GridList[0].ElectricFieldUpInf*(z-self.GridList[0].z_Location)    
            elif (z < self.GridList[ii].z_Location and z >= self.GridList[ii+1].z_Location):
                if np.abs(self.GridList[ii].Voltage0-self.GridList[ii].ElectricFieldDownInf*(z-self.GridList[ii].z_Location)-\
                    self.GridList[ii+1].Voltage0-self.GridList[ii+1].ElectricFieldUpInf*(z-self.GridList[ii+1].z_Location) ) < 1. :
                    return self.GridList[ii].Voltage0-self.GridList[ii].ElectricFieldDownInf*(z-self.GridList[ii].z_Location)
                elif z >0:
                    return self.GridList[ii].Voltage0-self.GridList[ii].ElectricFieldDownInf*(z-self.GridList[ii].z_Location)
                else:
                    return self.GridList[ii+1].Voltage0-self.GridList[ii+1].ElectricFieldUpInf*(z-self.GridList[ii+1].z_Location)

            elif (z <= self.GridList[-1].z_Location):
                return self.GridList[-1].Voltage0-self.GridList[-1].ElectricFieldDownInf*(z-self.GridList[-1].z_Location)


    def Copy(self):
        return LZ_detector(self.GridList)


    def Print(self,PrintLess= True):
        print "############################################################"
        print "############################################################"
        print "############################################################"
        print "############################################################"
        print "Number of Grid:", len(self.GridList)-2
        print "Print Less = ", PrintLess
        for i in range(len(self.GridList)):
            self.GridList[i].Print(PrintLess)
        print "############################################################"
        print "############################################################"
        print "############################################################"
        print "############################################################"

