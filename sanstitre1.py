import numpy
from random import *
def mot():
   a=numpy.loadtxt('U:/nathan.fauconet/nsi/projet/mot.txt', dtype=str)
   n=int(random()*len(a))
   print(a[n])
mot()   

