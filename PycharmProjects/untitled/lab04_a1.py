#Michael Waldron
#100657864
#was already marked as done just submitting as a backup
#copied code from lab description
partyNames=['Krogg','Glinda','Geoffrey']
partyHp= [180,120,150]
partyAttack = [20,5,15]
partyDefense=[20,20,15]
partyDead=[False,False,False]
bossAttack=25
bossDefense=15
bossHP=500
x=0

def isDead(a):
    if a<=0:
        return True
    else: return False
def isPartyDead():
    y=0
    for i in partyHp:
        if i<=0:
            y+=1
    if y==3:
        return True
H = isPartyDead()
#main while loop that checks if
while bossHP>0 or isPartyDead() == False :
    for members in partyNames:#Glinda healing the boys
        if members == 'Glinda' and isDead(partyHp[1]) == False:
            for member in partyHp:
                member += partyAttack[1]
            print('Glinda just healed everybody for 5 health')
    # the party members attacking the boss
    for mydudes in partyAttack:
        if(mydudes!=5):
            if mydudes == 20 and isDead(partyHp[0])==False:
                if isDead(partyHp[0])==False:
                 dmg1=mydudes-bossDefense
                 bossHP=bossHP-dmg1
                 print('krogg does', dmg1, ' damage to the boss')
            else:
                if isDead(partyHp[2]) == False:
                 dmg1 = mydudes - bossDefense
                 BossHP = bossHP - dmg1
                 print('Geoffrey does', dmg1, ' damage to the boss')
    print('the boss is almost dead his HP is ', bossHP)
    for HPbois in partyHp:# the boss smacking the party members loop
            if(bossHP>0):
                bdmg=bossAttack-partyDefense[x]
                HPbois = HPbois-bdmg
                #changing the value of party dead if the hp is below 0
                print('Boss does ', bdmg,' points of damage to', partyNames[x])
                #counter tells us what element the boss is attaking apart from the health
                if(x==2): x=0
                if(x!=2):x+=1
if(bossHP<=0): print("The boss is Dead")

