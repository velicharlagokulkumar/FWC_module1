import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          
sys.path.insert(0,'/sdcard/gokul/matrices/circle/codes/CoordGeo') 
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

import subprocess
import shlex

r = 5
O = np.array(([1,2]))
B=np.array(([1,7]))
D=np.array(([4,-2])) 
Z=np.array([[0,1],[3,-4]])
X=np.array([7,20])
C=LA.solve(Z,X)
h=LA.norm((B-C))
ar=0.5*2*r*h
#O = d*e1 #Centre
#P = np.array(([0,0]))
#theta = mp.asin(r/d)
#Q1 = r*mp.cot(theta)*np.array(([mp.cos(theta),mp.sin(theta)]))
#Q2 = r*mp.cot(theta)*np.array(([mp.cos(theta),-mp.sin(theta)]))
print("Area of quadrilateral is ", ar)
#Generating all lines
xBO = line_gen(B,O)
xOD = line_gen(O,D)
xBC = line_gen(B,C)
xDC = line_gen(D,C)
##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(xBO[0,:],xBO[1,:],label='$Radius$')
plt.plot(xOD[0,:],xOD[1,:],label='$Radius$')
plt.plot(xBC[0,:],xBC[1,:],label='$Tangent$')
plt.plot(xDC[0,:],xDC[1,:],label='$Tangent$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.vstack((O,B,D,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','B','D','C']
for i, txt in enumerate(vert_labels):
        plt.annotate(txt, # this is the text
                                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                                                  textcoords="offset points", # how to position the text
                                                                   xytext=(0,10), # distance from text to points (x,y)
                                                                                    ha='center') # horizontal alignment can be left, right or center

        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.legend(loc='best')
        plt.grid() 
        plt.axis('equal')

      
        plt.savefig('/sdcard/gokul/matrices/circle/images/matrix.pdf')
        subprocess.run(shlex.split("termux-open /sdcard/gokul/matrices/circle/images/matrix.pdf"))
   