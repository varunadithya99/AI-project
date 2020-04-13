from math import *
from numpy import *


def rms(train, test):
   sum = 0
   r, c = train.shape
   for i in range(r):
       for j in range(c):
           if test[i][j] != 0:
               sum += pow((test[i][j] - train[i][j]), 2)
   return sqrt(sum/count_nonzero(test))