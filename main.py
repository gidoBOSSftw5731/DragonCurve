#!/usr/bin/python3

import turtle as t
#from array import array
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
rounds = 4-1
t.color('red')
#True is Zig, False is Zag
directions = np.asarray([True, False])
t.speed(10000)
i=0
while 2 > i:
    arr=directions[:]
    #print(j)


    j = 0
    while j < len(arr):
        
        directions = np.insert(directions, j*2, not arr[j])
        j+=1     
 

    #left(90)
    
    i+=1
print(str(directions))


for i in directions:
    j=1
    if not i:
        j=-1
    t.left(90*j)
    
    t.forward(10)
t.done()
