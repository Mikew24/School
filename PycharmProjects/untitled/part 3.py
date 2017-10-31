def gainXP(xpgain,Character):
    o = Character.getLevel - 1
    levelminXP=[100,200,300,400,500]
    levelAttackGain=[5,7.5,10,12.5,15]
    levelDefenseGain=[2.5,5,7.5,10,15]
    levelMagicGain=[2,3,5,8,10]
    if(xpgain+Character.getXP() >= levelminXP[o]):
        Character.setXP =(Character.getXP+xpgain)-levelminXP[o]
        Character.setLevel += 1
        Character.setAttack = Character.getAttack+levelAttackGain[o]
        Character.setDefense = Character.getDefense + levelDefenseGain[o]
        Character.setMagic = Character.getMagic + levelMagicGain[o]
def battle(enemy,party):
    