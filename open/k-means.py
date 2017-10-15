# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:04:04 2017

@author: abhishekgadireddy
"""

import math
import random 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

y=datasets.load_iris()

iris=y.data[:150,:4]
x1=random.randint(0,149)
x2=random.randint(0,149)
x3=random.randint(0,149)

grp1=[]
grp2=[]
grp3=[]
classes=[]
for i in range(0,150):
    classes.append(-1)
    
def eucdistance(x1,x2,x3,iris,bool):
    for i in range(0,150):
      a=np.linalg.norm(x1-iris[i])
      b=np.linalg.norm(x2-iris[i])
      c=np.linalg.norm(x3-iris[i])
      if(a<b and a<c):
          grp1.append(iris[i])
          if classes[i]!=0 or classes[i]==-1:
              bool=1
          classes[i]=0
      elif(b<c and b<a):
          grp2.append(iris[i])
          if classes[i]!=1 or classes[i]==-1:
              bool=1
          classes[i]=1
      else:
          grp3.append(iris[i])
          if classes[i]!=2 or classes[i]==-1:
              bool=1
          classes[i]=2
      
    center1=np.mean(grp1, axis=0) 
    center2=np.mean(grp2, axis=0) 
    center3=np.mean(grp3, axis=0) 
    
    return center1,center2,center3,bool
bool=0
center1,center2,center3,bool=eucdistance(iris[x1],iris[x2],iris[x3],iris,bool) 
i=0
while bool==1:
    bool=0
    grp1=[]
    grp2=[]
    grp3=[]
    center1,center2,center3,bool=eucdistance(center1,center2,center3,iris,bool)
    i=i+1     
