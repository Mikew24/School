# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:55:28 2017

@author: Michael, 100657864
"""
""" fixed the spacing that was wrong"""
kroggName='Krogg'
kroggClass='Warrior'
kroggLevel=1
kroggAttack=18.5
kroggDefense=12.5
kroggHP=200
kroggXP=0
kroggWeapons=['Axe','Dagger','Unarmed']
krog=(kroggName,kroggClass,kroggLevel,kroggAttack,kroggDefense,kroggHP,kroggXP,kroggWeapons)
""" making the extra Characters"""
Character1='Glinda'
Class1='Spellcaster'
level1=1
Attack1=4.5
Defense1=25
Hp1=120
Xp1=0
Weapons1=['Staff','Unarmed']
Glinda=(Character1,Class1,level1,Attack1,Defense1,Hp1,Xp1,Weapons1)
Character2='Geoffrey'
Class2='Paladin'
level2=1
Attack2=15
Defense2=12.5
Hp2=180
Xp2=0
Weapons2=['Bow','Sword']
Geoffrey=(Character2,Class2,level2,Attack2,Defense2,Hp2,Xp2,Weapons2)
Character1='Dark Dragon'
Class1='Boss'
level1=10
Attack1=25
Defense1=17.5
Hp1=500
Xp1=1000
Weapons1=['Flame Breath']
Boss=(Character1,Class1,level1,Attack1,Defense1,Hp1,Xp1,Weapons1)
""" Creating the party that consists of the Krog, Geoffrey, and Glinda"""
party=[Geoffrey,Glinda,krog]
"""Changing tuples  of atacker and defender to lists so i can change the values within"""
krogls = list(krog)
Geoffreyl=list(Geoffrey)
"""making the krogs HP = the hp of the krog hp - the diffrence of the attakers attack and dfenders defense"""
print('HP b4 the attack',krogls[5])
krogls[5]=krogls[5]-(Geoffreyl[3]-krogls[4])
"""printing the Krogs Hp"""
print('krogs hp is now ',krogls[5])
"""updatng the values of the tuples"""
krog=tuple(krogls)
Geoffrey=tuple(Geoffreyl)