#Michael Waldron/100657864
#Character class
#copied and modified code from my assignment one which we decided to use classes for
class Character:
    #constructor sets magic to zero unless other specified
    def __init__(self, name, hp, xp, attack, defense,magic=0):
        self.name = name
        self.maxHP=hp
        self.hp = hp
        self.xp = xp
        self.attack = attack
        self.defense = defense
        self.magic=magic
       #prints character name and how much Hp they have
    def __str__(self):
        return self.name + ' has '+str(self.hp)+' HP'
    #checks if the a Character is dead
    def isDead(self):
        if self.hp<=0:
            return True
        return False
    """ heals party and makes sure hp does not exceed that characters initial full hp"""
    def heal(self, party):
        if not self.isDead():
            for healed in party:
                if not healed.isDead():
                    healed.hp += self.magic
                    print(self.name, 'healed', healed.name, 'for', self.magic, 'hp')
                    if healed.hp>healed.maxHP:
                        healed.hp = healed.maxHP
    #attack method which takes the attacking character and the victim as parameters
    def attacking(self, otherCharacter):
        if self.isDead():
            print(self.name, 'cannot attack because they are dead!')

        else:
            if otherCharacter.isDead()==False:
                damageDealt = self.attack - otherCharacter.defense
                if damageDealt <= 0:
                    damageDealt = 0
                otherCharacter.hp = otherCharacter.hp - damageDealt
                if otherCharacter.hp < 0:
                    otherCharacter.hp==0
                    print('you have slain the boss')
                if not otherCharacter.isDead():
                    print(self.name, 'does', damageDealt, 'points of damage to', otherCharacter.name)

#runs the .isdead() method for all characters in the party and returns True if they are all dead
def isPartyDead(party):
    y=0
    for i in party:
       if i.isDead()==True:
          y+=1
    if y==3:
        return True

#initializing Characters
krogg = Character ('Krogg',180,20,20,10)
glinda = Character ('Glinda', 120, 5, 20, 5,10)
geoffrey = Character ('Geoffrey', 150, 15, 15,10)
party = [krogg, glinda, geoffrey]
boss = Character('Boss', 500, 25, 15,10)
round = 1
#battle loop from code given
while (not boss.isDead()) and (not isPartyDead(party)):
    print('Round', round)

    # krogg attacks
    krogg.attacking(boss)
    # geoffrey attacks
    geoffrey.attacking(boss)
    # glinda heals
    glinda.heal(party)
    # boss attacks
    for partyMember in party:
        boss.attacking(partyMember)
        # show progress
    for partyMember in party:
        print(partyMember)
    print(boss)
    print('')
    round += 1
    if isPartyDead(party):
        print('Your whole party is dead.  You lose.')
    elif boss.isDead():
        print('The boss is dead.  You are victorious!')