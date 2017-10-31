# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:16:23 2017

@author: aidan
"""


class Animal:
    def __init__(self, mass):
        # good practice to write
        super().__init__()
        print('Animal.__init__()')
        # ^^
        self.mass = mass


class Friend:
    def __init__(self):
        super().__init__()
        print('Friend.__init__()')
        self.years = 0;


class Dog(Animal, Friend):
    species = 'canine Domesticus'

    def __init__(self, mass, name):
        super().__init__(mass)
        print('Dog.__init__()')
        self.name = name

    def __lt__(self, other):
        return self.mass < other.mass


fido = Dog(2.1, 'fido')
spot = Dog(4.9, 'spot')