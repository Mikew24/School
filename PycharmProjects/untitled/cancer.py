class Character:
    def __init__(self, name, hp, xp, attack, defense, magic=0, level=0):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.maxHP = hp
        self.attack = attack
        self.defense = defense
        self.magic = magic

        self.level = level

    def getXP(self):
        return self.xp

    def isDead(self):
        if self.hp <= 0:
            return True
        return False

    def attack(self, victum):
        if self.isDead(self):
            print(self.name, 'cannot attack because they are dead!')
        else:
            damageDealt = self.attack - victum.defense
            victum.hp = victum.hp - damageDealt
            if victum.hp < 0:
                victum.hp = 0
            print(self.name, 'does', damageDealt, 'points of damage to', victum.name)

    def heal(self, party):
        for healed in party:
            if not healed.isDead():
                healed.hp += self.magic
                if healed.hp > healed.maxHP:
                    healed.hp = healed.maxHP
            print(self.name, 'healed', healed.name, 'for', self.magic, 'hp')

    def __str__(self):
        # return '',self.name , self.hp , self.level , self.xp  , self.attack  ,self.defense
        return self.name + ' has ' + str(self.hp) + ' HP.'


loops = 0
krogg = Character('Krogg', 180, 0, 20, 20, 0)
glinda = Character('Glinda', 120, 0, 5, 20, 5)
geoffrey = Character('Geoffrey', 150, 0, 15, 15)

party = [krogg, glinda, geoffrey]

enemy1 = Character('Spider 1', 50, 100, 10, 1)
enemy2 = Character('Spider 2', 50, 100, 10, 1)
enemy3 = Character('Wolf 1', 100, 250, 15, 5)
enemy4 = Character('Wolf 2', 100, 250, 15, 5)
enemy5 = Character('Bear 1', 200, 350, 20, 10)
enemy6 = Character('Bear 2', 200, 350, 20, 10)
enemy7 = Character('Red Dragon', 300, 800, 30, 20)
enemy8 = Character('Blue Dragon', 400, 1000, 35, 20)

enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7,
           enemy8]

def op (party, enemies):
    x=0
    y = 1
    for enemys in enemies:
        while enemys.getHP>0:
         if(party[0].getHP>0):
          party[0].attack(enemys)
         if (party[1].getHP > 0):
             for members in party:
                 glinda.heals(members)
         if (party[2].getHP > 0):
             party[2].attack(enemys)
         if(enemys.getHP>0)   :
            for members in party:
             enemys.attack(members)
         for members in party:
             if members.getHp>0:
                 gainXP(enemys.getXPGained,members)

def gainXP(xpgain, Character):
    o = Character.getLevel - 1
    levelminXP = [100, 200, 300, 400, 500]
    levelAttackGain = [5, 7.5, 10, 12.5, 15]
    levelDefenseGain = [2.5, 5, 7.5, 10, 15]
    levelMagicGain = [2, 3, 5, 8, 10]
    if(Character.getLevel<6):
      if (xpgain + Character.getXP() >= levelminXP[o]):
        Character.setXP = (Character.getXP + xpgain) - levelminXP[o]
        Character.setLevel += 1
        Character.setAttack = Character.getAttack + levelAttackGain[o]
        Character.setDefense = Character.getDefense + levelDefenseGain[o]
        Character.setMagic = Character.getMagic + levelMagicGain[o]


print(Character.getXP(krogg))
print(Character.__str__(krogg))