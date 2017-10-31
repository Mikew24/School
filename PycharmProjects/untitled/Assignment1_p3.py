class Character:
    """
    Constructor For mainly the party members because we have to worry about
    all traits like magic and level
    """
    #self = this
    def __init__ (self, name, hp, xp, attack, defense, level=1, magic=0):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.maxHP = hp
        self.attack = attack 
        self.defense = defense
        self.magic = magic
        self.level = level
        #Mainly for enemies
        """
        Mainly for the enemies because it is more basic and has the essentials
        so this constructor is overloading the previous but this one is only used on 
        enemies
        """
    def __intit__(self, name, hp, xp, attack, defense):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.attack = attack
        self.defense = defense
        
# Getters used in other segments of code
    def getXP(self):
        return self.xp
    def getLevel(self):
        return self.level
    def getHP(self):
        return self.hp
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getName(self):
        return self.name
    def getMagic(self):
        return self.magic
    
# Setters used in other segments of code
    def setLevel(self, level):
        self.level = level
    def setHP(self, hp):
        self.hp = hp
    def setXP(self, xp):
        self.xp = xp
    def setMagic(self, magic):
        self.magic = magic
    def setAttack(self, attack):
        self.attack = attack
    def setDefense(self, defense):
        self.defense = defense
        """
isDead function checks if the player is dead and returns a boolean statment
true if they are false if not
"""
    def isDead(self):
        if self.hp<=0:
            return True
        return False
    """
    pretty much a setter but uses the victum so we can access the 
    victums xp value to add it to the party if they kill them
    """
    def gainXP(self,victum):
        
        if not self.isDead():
            #print(self.getName() + ' did not gain xp because they are dead!')
            newXP = self.getXP() + victum.getXP()
            self.setXP(newXP)
            #print("memes")
            """
attack power checks if the fighter is dead or not and if they arent
we attack the victum using self attack and if they are dead then we wont bother attacking them
"""  
    def attackPower(self, victum):
        if self.isDead():
            print(self.name , 'cannot attack because they are dead!')
        else:
            damageDealt = self.attack - victum.defense
            if damageDealt<0:
                damageDealt = 0
            victum.setHP(victum.getHP()-damageDealt)
            if victum.getHP()<0:
                victum.setHP(0)
            if not victum.isDead():
                print(self.name, 'does' , damageDealt, 'points of damage to', victum.name)
                
                """
                Heal is glindas attack she heals the entire party for her magic
                and if they are at there cap hp then she cannot heal them
                """
            
    def heal(self, party):
        if not self.isDead():
            for healed in party:
                if not healed.isDead():
                    healed.hp += self.magic
                    print(self.name, 'healed', healed.name, 'for', self.magic, 'hp')
                    if healed.hp>healed.maxHP:
                        healed.hp = healed.maxHP
                        print(healed.getName(), "could not be healed!")
                else:
                    print(healed.getName(), "could not be healed!")
            """
            Returns a clean statment of all the stats put in the constructor
            but if the character is dead it returns just the name then [DEAD] beside it
            """
    def __str__(self):
        if self.getHP()<=0:
            return self.name + '[DEAD]'
        return self.name + ' (HP:'+ str(self.getHP()) + ', XP:' + str(self.getXP()) + ', Level:' + str(self.getLevel()) + ', Attack:' + str(self.getAttack()) + ', Defense:' + str(self.getDefense()) + ')'
       # return self.name + ' has ' + str(self.hp) + ' HP.'
#self, name, hp, xp, attack, defense, level=1, magic=0):  
    
    
"""
Variables used
declared each character and the used the two different constructors
"""
loops = 0
krogg = Character('Krogg', 180, 0, 20, 10)
#the extra 1 , 5 last two values are 
# level and magic
glinda = Character('Glinda', 120, 0, 5, 10,1, 5)
geoffrey = Character('Geoffrey', 150,0,15,10)

#List of Characters
party = [krogg, glinda, geoffrey]
           
enemy1 = Character('Spider 1', 50, 100, 10, 1)
enemy2 = Character('Spider 2', 50, 150, 10, 1)
enemy3 = Character('Wolf 1', 100, 250, 15, 5)
enemy4 = Character('Wolf 2', 100, 300, 15, 5)
enemy5 = Character('Bear 1', 200, 350, 20, 10)
enemy6 = Character('Bear 2', 200, 400, 20, 10)
enemy7 = Character('Red Dragon', 300, 800, 30, 25)
enemy8 = Character('Blue Dragon', 400, 1000, 35, 25)
#list of enemies
enemies = [enemy1, enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8]
"""
Prints the stats to the console
"""
def readStats(party, enemies):
    for p in party:
        print(p)

    print(enemies)


    """
     This is the fighting method
        All actions take place in the method
        Loops through all the enemies 
        and we attack as long as the HP larger than 0
        if the entire party is killed print the party was defeated
        """


def doAction(party, enemies):
    #First loop
    #e = spider1
    #p = Krogg
    loop = 1
    count = 0
    lose = False
    for e in enemies:
        # Add Condition That Chooses that breaks out if enemys kill part            
        while e.getHP()>0 and lose == False:
            print(" ")
            print("Round:", loop)
            if party[0].isDead() and party[1].isDead() and party[2].isDead():
                lose = True
            for p in party:
                if not p.getName() == 'Glinda':
                    p.attackPower(e)
                else:
                    p.heal(party)
            for p in party:
                e.attackPower(p)
            loop +=1
            print(" ")
            print("Status:")
            readStats(party,e)
            input("proceed to next round press enter")
        for p in party:
            if p.isDead():
                print(p.getName() + " has been defeated!")
            p.gainXP(e)
            levelUp(p)
        for dead in enemies:
            if dead.isDead():
                count +=1

        if count>len(enemies)+1:
            print("-----------------------------------------")
            print("ALL ENEMIES DEFEATED, YOU ARE VICTORIOUS")
            print("-----------------------------------------")
        

        if lose:
            print("The party has been defeated you lose!")
            break
        
def statChange(p,level,getXP):
   #levelminXP = [100, 250, 500, 1000, 1500]
    levelAttackGain = [2, 2.5, 2.5, 2.5, 2.5]
    levelDefenseGain = [1.5, 1.5, 2, 2, 2]
    levelMagicGain = [0.5, 0.5, 0.5, 1, 1]
    arrayPos = level-2
    p.setLevel(level)
    p.setAttack(p.getAttack()+levelAttackGain[arrayPos])
    p.setDefense(p.getDefense() + levelDefenseGain[arrayPos])
    """
    if level == 2:
        p.setXP(getXP-levelminXP[0])
    elif level == 3:
        p.setXP(getXP-levelminXP[1])
    elif level == 4:
        p.setXP(getXP-levelminXP[2])
    elif level == 5:
        p.setXP(getXP-levelminXP[3])
    elif level == 6:
        p.setXP(getXP-levelminXP[4])
   """
    if p.getName() == 'Glinda':
        p.setMagic(p.getMagic() + levelMagicGain[arrayPos])
    
def levelUp(p):
    levelminXP = [100, 350, 850, 1850, 3350]

    if(p.getLevel()<6):
        #print("Memes")
        if(p.getXP()>=levelminXP[0] and p.getXP()<levelminXP[1]):
            statChange(p,2, p.getXP())
            print("***LEVEL 2***")
        elif(p.getXP()>=levelminXP[1] and p.getXP()<levelminXP[2]):
            statChange(p,3,p.getXP())
            print("***LEVEL 3***")
        elif(p.getXP()>=levelminXP[2] and p.getXP()<levelminXP[3]):
            statChange(p,4,p.getXP())
            print("***LEVEL 4***")
        elif(p.getXP()>=levelminXP[3] and p.getXP()<levelminXP[4]):
            statChange(p,5,p.getXP())
            print("***LEVEL 5***")        
        elif(p.getXP()>=levelminXP[4]):
            statChange(p,6,p.getXP())
            print("***LEVEL 6***")
    else:
        return False
doAction(party, enemies)