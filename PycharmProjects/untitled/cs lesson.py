# -*- coding: utf-8 -*-
def kek(num):
    print ('d')
print ('done')
def recursivecancer(num):
    if(num==1):
        return 1
    if(num==0):
        return 0
    return num+recursivecancer(num-1)

print(recursivecancer(5))
