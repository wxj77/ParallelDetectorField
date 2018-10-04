# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:57:05 2017

@author: wei
"""
# This is not based on data from 20170418_03_GateWireOnlyNewMakeGeo2.mph
# This is based on data from 20170418_04_GateWireOnlyNewMakeGeoMesh01,02.mph
#filestr ="01"
fignum = 40
workdir ="/media/wei/ACA8-1ECD/ComsolGeoFile/"
import sys
sys.path.insert(0, "/media/wei/ACA8-1ECD/SystemTest//XenonProperty/")
sys.path.insert(0, workdir)
import unit

from ComsolSurfaceField import *
import scipy as sp
from scipy.interpolate import griddata
from scipy import interpolate
from scipy import integrate
from scipy.integrate import simps
import math
import scipy.optimize as opt

EFieldOnSurfaceDetail1Origin = np.loadtxt(workdir+"EFieldOnSurfacesDetail1"+filestr+".txt", skiprows = 9)
#EFieldOnSurfaceDetail1Origin = np.append(EFieldOnSurfaceDetail1Origin, -EFieldOnSurfaceDetail1Origin[:,3:], axis=1)
EFieldOnSurfaceDetail2Origin = np.loadtxt(workdir+"EFieldOnSurfacesDetail2"+filestr+".txt", skiprows = 9)
#EFieldOnSurfaceDetail2Origin = np.append(EFieldOnSurfaceDetail2Origin, -EFieldOnSurfaceDetail2Origin[:,3:], axis=1)
Radius_Gate = 37.5*unit.u
offset_Gate = 1.*unit.u
Pitch_Gate = 5.*unit.m

Ro_Gate = Radius_Gate + offset_Gate 

x1 = EFieldOnSurfaceDetail1Origin[:,0]*unit.u
y1 = EFieldOnSurfaceDetail1Origin[:,1]*unit.u
z1 = EFieldOnSurfaceDetail1Origin[:,2]*unit.u
oz1 = Ro_Gate - np.abs(2.*Ro_Gate/Pitch_Gate * x1) 

Theta1 = np.vectorize(math.atan2)((z1-oz1),y1)
X1 = x1/Pitch_Gate * (Pitch_Gate**2+(2.*Ro_Gate)**2)**0.5
Y1 = Radius_Gate * (Theta1)

Array_ER1 = np.empty((np.shape(EFieldOnSurfaceDetail1Origin)[0],len(E_Bot1)))
Array_Eabs1 = np.empty((np.shape(EFieldOnSurfaceDetail1Origin)[0],len(E_Bot1)))
Array_EX1 = np.array([])
Array_EY1 = np.array([])
for ii in range(len(E_Bot1)):
#for ii in range(1):
    E_BT = EFieldOnSurfaceOrigin[ii,3] 
    Theta = Theta1
    Phi = np.arctan(2. * Ro_Gate/ Pitch_Gate)
    Ex = EFieldOnSurfaceDetail1Origin[:,3*ii+3]/E_BT 
    Ey = EFieldOnSurfaceDetail1Origin[:,3*ii+4]/E_BT  
    Ez = EFieldOnSurfaceDetail1Origin[:,3*ii+5]/E_BT  
    ER = Ey* np.cos(Theta)* np.cos(Phi) + Ez* np.sin(Theta)* np.cos(Phi) - Ex* np.sin(Phi) 
    Array_ER1[:,ii] = ER
    Array_Eabs1[:,ii] = (Ex**2+Ey**2+Ez**2)**(0.5)
    del Ex, Ey, Ez, ER
del x1,y1,z1,oz1
Array_ER1 = Array_ER1[:,sort_index]
Array_Eabs1 = Array_Eabs1[:,sort_index]

x2 = EFieldOnSurfaceDetail2Origin[:,0]*unit.u
y2 = EFieldOnSurfaceDetail2Origin[:,1]*unit.u
z2 = EFieldOnSurfaceDetail2Origin[:,2]*unit.u
oz2 = -( Ro_Gate - np.abs(2.*Ro_Gate/Pitch_Gate * y2)) 

Theta2 = np.vectorize(math.atan2)((z2-oz2),x2)
X2 = y2/Pitch_Gate * (Pitch_Gate**2+(2.*Ro_Gate)**2)**0.5
Y2 = Radius_Gate * (Theta2)
 
Array_ER2 = np.empty((np.shape(EFieldOnSurfaceDetail2Origin)[0],len(E_Bot1)))
Array_Eabs2 = np.empty((np.shape(EFieldOnSurfaceDetail2Origin)[0],len(E_Bot1)))
Array_EX2 = np.array([])
Array_EY2 = np.array([])
for ii in range(len(E_Bot1)):
#for ii in range(1):
    E_BT = EFieldOnSurfaceOrigin[ii,3]
    Theta = Theta2
    Phi = np.arctan(2. * Ro_Gate/ Pitch_Gate)
    Ex = EFieldOnSurfaceDetail2Origin[:,3*ii+3]/E_BT 
    Ey = EFieldOnSurfaceDetail2Origin[:,3*ii+4]/E_BT  
    Ez = EFieldOnSurfaceDetail2Origin[:,3*ii+5]/E_BT  
    ER = Ex* np.cos(Theta)* np.cos(Phi) + Ez* np.sin(Theta)* np.cos(Phi) + Ey* np.sin(Phi) 
    Array_ER2[:,ii] = ER
    Array_Eabs2[:,ii] = (Ex**2+Ey**2+Ez**2)**(0.5)
    del Ex, Ey, Ez, ER
del x2,y2,z2,oz2
Array_ER2 = Array_ER2[:,sort_index]
Array_Eabs2 = Array_Eabs2[:,sort_index]

array_x = np.linspace(0, Pitch_Gate,201)
array_y = np.linspace(-np.pi,np.pi,19)*Radius_Gate
array_x1 = 0.5*(array_x[1:]+array_x[:-1])
array_y1 = 0.5*(array_y[1:]+array_y[:-1])
grid_x1, grid_y1 = np.meshgrid(array_x1,array_y1)


X = np.append(-X1, Pitch_Gate+X2)
Y = np.append(Y1,Y2)
Array_ER = np.append(Array_ER1,Array_ER2, axis= 0)
points = np.array([X,Y]).T
values = Array_ER
grid_z1 = griddata(points, values, (grid_x1, grid_y1), method='linear')

del points, values

grid_z2 = np.copy(grid_z1)
for ii in range(np.shape(grid_z2)[2]):
    grid_z2[:,:,ii] = grid_z1[:,:,ii]/(Ratio1[ii]-1)


# Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1, projection='3d')
#ax1.plot_trisurf(X/unit.m, Y/unit.u, Array_ER[:,0], linewidth=0.2, antialiased=True)
ax1.plot_wireframe(grid_x1/unit.m, grid_y1/unit.u, grid_z1[:,:,0], linewidth=0.2, antialiased=True, color ="r")
ax1.plot_wireframe(grid_x1/unit.m, grid_y1/unit.u, grid_z1[:,:,30], linewidth=0.2, antialiased=True, color ="g")
ax1.plot_wireframe(grid_x1/unit.m, grid_y1/unit.u, grid_z1[:,:,60], linewidth=0.2, antialiased=True, color ="b")
ax1.set_xlabel("Distance along the wire (mm)")
ax1.set_ylabel("Circumsance around the wire (um)")
ax1.set_zlabel("E (unit)")
ax1.set_title("Wire Surface Field: E_Bot = 1 unit \n Pitch_Gate = 5 mm, Radius_Gate =37.5 um")

plt.legend(loc=1)
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end

# Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1, projection='3d')
#ax1.plot_trisurf(X/unit.m, Y/unit.u, Array_ER[:,0], linewidth=0.2, antialiased=True)
ax1.plot_wireframe(grid_x1/unit.m, grid_y1/unit.u, grid_z1[:,:,10]/(Ratio1[10]-1), linewidth=0.2, antialiased=True, color ="r", label = "E_Top/E_Bot ="+str(Ratio1[10]))
ax1.plot_wireframe(grid_x1/unit.m, grid_y1/unit.u, grid_z1[:,:,25]/(Ratio1[25]-1), linewidth=0.2, antialiased=True, color ="g", label = "E_Top/E_Bot ="+str(Ratio1[25]))
ax1.plot_wireframe(grid_x1/unit.m, grid_y1/unit.u, grid_z1[:,:,60]/(Ratio1[60]-1), linewidth=0.2, antialiased=True, color ="b", label = "E_Top/E_Bot ="+str(Ratio1[60]))
angle =90
ax1.view_init(30, angle)
#for angle in range(0, 360):
#    ax1.view_init(30, angle)
#    plt.draw()
#    plt.pause(.001)
ax1.set_xlabel("Distance along the wire (mm)")
ax1.set_ylabel("Circumsance around the wire (um)")
ax1.set_zlabel("E (unit)")
ax1.set_title("Wire Surface Field: E_Bot = 1 unit\n Pitch_Gate = 5 mm, Radius_Gate =37.5 um")

plt.legend(loc=1)
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end


# Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
ax1.plot(E_Top1,(np.average(np.average(grid_z1,axis=1),axis=0))/(Ratio1-1.), "ro-", label = "|E| Field on Wire Surface Average")
ax1.plot(E_Top1,np.abs((np.min(np.min(np.abs(grid_z1),axis=1),axis=0))/(Ratio1-1.)), "bo-", label = "|E| Field on Wire Surface Minimum")
ax1.plot(E_Top1,np.abs((np.max(np.max(np.abs(grid_z1),axis=1),axis=0))/(Ratio1-1.)), "go-", label = "|E| Field on Wire Surface Maximum")

#ax1.plot(Ratio1,np.mean(np.abs(Array_ER1), axis=0)/np.abs(Ratio1-1.), "r<-", label = "E Field on Wire Surface Average")
#ax1.plot(Ratio1,np.min(np.abs(Array_ER1), axis=0)/np.abs(Ratio1-1.), "b<-", label = "|E| Field on Wire Surface Minimum")
#ax1.plot(Ratio1,np.max(np.abs(Array_ER1), axis=0)/np.abs(Ratio1-1.), "g<-", label = "|E| Field on Wire Surface Maximum")

ax1.set_xlabel("E_Top (unit)")
ax1.set_ylabel("E (unit)")
ax1.set_xlim(-50,50)
ax1.set_ylim(-5,25)

ax1.set_title("Wire Surface Field: E_Bot = 1 unit\n Pitch_Gate = 5 mm, Radius_Gate =37.5 um")

plt.legend(loc=1)
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end

# Plot start
a=plt.figure(fignum, figsize=(9,7))
ax1=plt.subplot(1,1,1)
#exclude those numbers with E_Top/E_Bot close to 1 
def f_test8(a, x, y):
    cons = 2.5*unit.m
    return -y + a[0] + a[1]*(x- cons)**2 + a[2]*(x-cons)**4+ a[3]*(x-cons)**6+ a[4]*(x-cons)**8 
def f_test6(a, x, y):
    cons = 2.5*unit.m
    return -y + a[0] + a[1]*(x- cons)**2 + a[2]*(x-cons)**4+ a[3]*(x-cons)**6
def f_test4(a, x, y):
    cons = 2.5*unit.m
    return -y + a[0] + a[1]*(x- cons)**2 + a[2]*(x-cons)**4
def f_test2(a, x, y):
    cons = 2.5*unit.m
    return -y + a[0] + a[1]*(x- cons)**2
    
def f_test2cos(a, x, y):
    cons = 2.5*unit.m
    return -y + a[0] + a[1]*np.cos((x- cons)/a[2])
    
#excludelist = [42,43,44,45,46,47,48,49,50]
excludelist = range(55,60)
for ii in range(np.shape(grid_z2)[2]):
    if ii not in excludelist:
#    if ii==78:
        ax1.plot(array_x1/unit.m, (np.average(grid_z2,axis=0))[:,ii],linewidth=0.2)#, label = "%.2f"%(Ratio1[ii]))
 
        x0 = np.array([4.3,8.3,5.*unit.m*np.pi])#,1.e16,1.e20])        
        optresult = opt.least_squares(f_test2cos, x0,args=(array_x1,(np.average(grid_z2,axis=0))[:,ii]))
        z = np.polyfit(array_x1,(np.average(grid_z2,axis=0))[:,ii], 6)
        if ii==np.shape(grid_z2)[2]-1:        
            ax1.plot(array_x1/unit.m, f_test2cos(optresult.x, array_x1, 0), linewidth =2, color="k", linestyle=":", label = "cosine")
        print optresult.x
       
        x0 = np.array([12.3,0.3])#,1.e16,1.e20])        
        optresult = opt.least_squares(f_test2, x0,args=(array_x1,(np.average(grid_z2,axis=0))[:,ii]))
        z = np.polyfit(array_x1,(np.average(grid_z2,axis=0))[:,ii], 6)
        if ii==np.shape(grid_z2)[2]-1:        
            ax1.plot(array_x1/unit.m, f_test2(optresult.x, array_x1, 0), linewidth =2, color="b", linestyle=":", label = "2nd order poly")
        print optresult.x
        
        x0 = np.array([12.3,0, -1.e12,])  
        optresult = opt.least_squares(f_test4, x0,args=(array_x1,(np.average(grid_z2,axis=0))[:,ii]))
        z = np.polyfit(array_x1,(np.average(grid_z2,axis=0))[:,ii], 6)
        if ii==np.shape(grid_z2)[2]-1:        
            ax1.plot(array_x1/unit.m, f_test4(optresult.x, array_x1, 0), linewidth =2, color="r", linestyle=":", label = "4th order poly")
        print optresult.x
        
        x0 = np.array([12.3,0, -1.e12,1.e16])  
        optresult = opt.least_squares(f_test6, x0,args=(array_x1,(np.average(grid_z2,axis=0))[:,ii]))
        z = np.polyfit(array_x1,(np.average(grid_z2,axis=0))[:,ii], 6)
        if ii==np.shape(grid_z2)[2]-1:        
            ax1.plot(array_x1/unit.m, f_test6(optresult.x, array_x1, 0), linewidth =2, color="g", linestyle=":", label = "6th order poly\n y = %.3e\n+%.3e(x-2.5e-3)^2\n+%.3e(x-2.5e-3)^4\n+%.3e(x-2.5e-3)^6"%(optresult.x[0],optresult.x[1],optresult.x[2],optresult.x[3]))
            EFieldFitPoly6 = np.copy(optresult.x)
        print optresult.x
        
        x0 = np.array([12.3,0, -1.e12,1.e16,1.e20])  
        optresult = opt.least_squares(f_test8, x0,args=(array_x1,(np.average(grid_z2,axis=0))[:,ii]))
        z = np.polyfit(array_x1,(np.average(grid_z2,axis=0))[:,ii], 6)
        if ii==np.shape(grid_z2)[2]-1:        
            ax1.plot(array_x1/unit.m, f_test8(optresult.x, array_x1, 0), linewidth =2, color="y", linestyle=":", label = "8th order poly\n y = %.3e\n+%.3e(x-2.5e-3)^2\n+%.3e(x-2.5e-3)^4\n+%.3e(x-2.5e-3)^6\n+%.3e(x-2.5e-3)^6"%(optresult.x[0],optresult.x[1],optresult.x[2],optresult.x[3],optresult.x[4]))
            EFieldFitPoly8 = np.copy(optresult.x)
        print optresult.x
        
        
ax1.set_xlabel("Distance along the wire (mm)")
ax1.set_ylabel("E (unit)")
ax1.set_title("Wire Surface Field: E_Top- E_Bot = 1 unit\n Pitch_Gate = 5 mm, Radius_Gate =37.5 um")
ax1.axhline(1.*Pitch_Gate/(2.*np.pi*Radius_Gate)/2.,label ="Uniform Field Prediction")

#plt.legend(loc=1)
# Shrink current axis by 20%
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax1.grid(True)
plt.savefig(workdir+str(fignum)+".png")
fignum = fignum+1
#Plot end


plt.show()




































