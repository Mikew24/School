# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:11:21 2017

@author: Michael
"""

def intersect(s1,s2):
    intersected =[]
    for x in s2:
        for y in s1:
            if y==x:
                print(y," ",x)
               # intersected=intersected+x
                intersected.insert(len(intersected),x)
    return intersected
 
list1=[1,4,5,7,9,11,13,15,17,19,21,23,25]
list2=[1,4,9,16,25]
print(intersect(list1, list2))