# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 03:48:40 2017

@author: Michael
"""

kdk = 'hello'
k=1.32
kk =(kdk, k)
print(kk)

def meth(num1):
        if num1 ==0:
            return 0
        if num1 ==1:
            return 1
        return num1 * meth(num1-1)
d= meth(10)
print(d)
print('please type in the number of iterations')
nums=input()
numm=float(nums)


def pishit(iterations):
    d=0
    y=1
    s=0
    x=0
    while d<iterations:
      if x%2==0:
          s=s+(4/y)
      if x%2!=0:
           s=s-(4/y)
      d=d+1
      y=y+2
      x=x+1
    return round(s,6)  
print(pishit(numm))


#print(pishit(100000))
  
        
