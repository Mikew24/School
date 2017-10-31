# -*- coding: utf-8 -*-
#dictionary is a relationshhip between a name and a value example michaelgpa = 4.0
#dictinary['michaelsgpa'] will return the double 4.0
'''
for element in dictinary:
    print(element)
'''

def ispalindrome(string):
    reverse=''
    for ch in string:
        reverse=ch+reverse

    print(reverse)
print(ispalindrome('racecar'))
def ispali(string):
    startIndex=0
    endIndex=len(string)-1

    while startIndex < endIndex:
        if string[startIndex]!=string[endIndex]:
         return False
        startIndex+=1
        endIndex-=1
    return True
print(ispali('adda'))
def palirecursive(string):
    if len(string)<=1:
        return True

    if string[-1]!=string[0]:
        return False
    return palirecursive(string[1:-1])
