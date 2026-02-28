#Python - Plotting of theoretical non-dim. temperatures on a heat map contour
import matplotlib.pyplot as plt
from ctypes import CDLL, c_int, c_double, POINTER
import numpy as np

lib = CDLL('./mylibrary.so') #Code written in C to calculate non-dim. temperature.
lib.nonDimTemp.argtypes = [c_double,c_double,c_double,c_double,c_int]
lib.nonDimTemp.restype = c_double

def HeatMapContour_TH():
    W = 1   #Non-Dim. Lengths
    L = 1 
    x1 = np.linspace(0, L, 100)
    y1 = np.linspace(0, W, 100)
    result_array_TH = np.zeros((len(x1),len(y1)))

    for i in range(len(x1)):
        for j in range(len(y1)):
            result_array_TH[i,j] = lib.nonDimTemp(x1[i],L,y1[j],W,1000)
            
    result_array_TH = np.rot90(result_array_TH)

    contour = plt.contourf(x1,y1,result_array_TH,levels=20)
    plt.colorbar(contour, label='Non-Dimensional Temperature')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Non-Dimensional Temperature Distribution Over A Flat Plate')
    plt.show()
 
 
 


HeatMapContour_TH()
