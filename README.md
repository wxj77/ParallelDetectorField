# ParallelDetectorField

##How to run this

* clone the repository
```
git clone git@github.com:wxj77/ParallelDetectorField.git
```

* update "LZ_Baseline_Detector.py" 
(1) create the detector geometry (LZ) from a list of grids (GridList).
    
```
import CalculateField as cf
...
LZ= cf.LZ_detector(GridList)
```
    
** The detector consists of several parallel planes on the z axis. These planes must be a decreasing function.
** all units are in SI: m, N, kg, Pa, etc.
** z=0 is liquid-gas interface. 
** Each plane could be a plane (P), parallel wire(PW), or woven wire (WM) with other wire specificated parameters.
    
(2) assign the voltages with a list of voltage (VList), the number of elements in the voltage list = the number of grids.
    
```
VList=[-1.5e3,5.75e3,-5.75e3,-50e3,-1.5e3,-1.5e3,]
LZ.UpdateVoltage(VList)
```
    
(3) get voltage at a location (x) with 

```
LZ.GetVoltageInZLocation(x)
```

(4) get electric field on the top/bottom/surface of the Nth grid by with 

```
LZ.GridList[N].ElectricFieldUpInf
LZ.GridList[N].ElectricFieldDownInf
LZ.GridList[N].SurfaceFieldNaive()
```


* run the code 
```
python .py
```





