library(KernSmooth)
library(ggplot2)
library(MASS)
library("asbio")
library("akima")
library(rgl)
library(scatterplot3d)
library(stats)
library(McSpatial)
library(ISLR)
library(MASS)
library(utils)

XenonSaturationTable= read.table("/media/wei/ACA8-1ECD/SystemTest/XenonProperty/fluid.txt",skip=1)
colnames(XenonSaturationTable) = c("Temperature (K)",	"Pressure (MPa)","	Density (l, mol/l)",	
                "Volume (l, l/mol)", "Internal Energy (l, kJ/mol)",	"Enthalpy (l, kJ/mol)",	
                "Entropy (l, J/mol*K)", "Cv (l, J/mol*K)",	"Cp (l, J/mol*K)",	
                "Sound Spd. (l, m/s)", "Joule-Thomson (l, K/MPa)",	"Viscosity (l, uPa*s)",	
                "Therm. Cond. (l, W/m*K)", "Surf. Tension (l, N/m)",	"Density (v, mol/l)",	
                "Volume (v, l/mol)", "Internal Energy (v, kJ/mol)",	"Enthalpy (v, kJ/mol)",	
                "Entropy (v, J/mol*K)", "Cv (v, J/mol*K)",	"Cp (v, J/mol*K)",	
                "Sound Spd. (v, m/s)", "Joule-Thomson (v, K/MPa)",	"Viscosity (v, uPa*s)",	
                "Therm. Cond. (v, W/m*K)")

