<<<<<<< HEAD
import numpy as np


#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

#Rotation Matrix
def rot(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return  np.array([[c,-s],[s,c]]) 


=======
import numpy as np


#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

#Rotation Matrix
def rot(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return  np.array([[c,-s],[s,c]]) 


>>>>>>> 0304b8968c69fc7d934bc0a86225b4b2742e528a
