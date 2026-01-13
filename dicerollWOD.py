#CREDIT GOES TO JACOB CONNOR AND CAIT MACLEON

import random

def rollsDisplay(rolls,successes,explodedRolls,explodeCount): 
    print("You rolled",len(rolls), "dice")
    print(sorted(rolls, reverse = True),"\n")
    print("You rolled",explodeCount,"explosion(s)")
    print(sorted(explodedRolls, reverse = True),"\n")
    print("You rolled",successes,"success(es)")
    allSuccesses = [i for i in rolls if i >=8]
    allExpSuccesses = [i for i in explodedRolls if i >= 8]
    if len(allExpSuccesses) >= 1:
        allSuccesses.append(allExpSuccesses)
    print(allSuccesses)
    if len(allSuccesses) >= 5:
        print("CRITICAL SUCCESS!")
    
    
    
'''def chanceDice(num_dice,num_sides):
    print("CHANCE TIME!")
    chanceRoll = []
    explodedChance = []
    chance_Roll = random.randint(1,num_sides)
    chanceRoll.append(chance_Roll)
    if chance_Roll == num_sides:
        exploded_Roll = random.randint(1,num_sides)
        explodedChance.append(exploded_Roll)
    if chance_Roll == 1:
        print("CRITICAL FAILURE!")
    print(chanceRoll)
    print(explodedChance)'''
        
def rollTheDice(num_dice,num_sides):
    rolls = []
    explodedRolls = []
    chanceRoll = []
    explodedChance = []
    explodeCount = 0
    successes = 0
    for i in range(num_dice):
        roll = random.randint(1,num_sides)
        rolls.append(roll)
        if roll >= 8:
            successes += 1
        
        if roll == num_sides:
            explodeCount += 1
            explodedRoll = random.randint(1,num_sides)
            explodedRolls.append(explodedRoll)
            if explodedRoll >= 8:
                successes += 1
            if explodedRoll == num_sides:
                explodeCount += 1
                explodedRoll = random.randint(1,num_sides)
                explodedRolls.append(explodedRoll)
    rollsDisplay(rolls,successes,explodedRolls,explodeCount)
    

    

def main():
    num_dice = 10 #int(input("How many dice would you like to roll? \n"))
    num_sides = 10
    if num_dice > 0:
        rollTheDice(num_dice,num_sides)
    elif num_dice == 0:
        chanceDice(num_dice,num_sides)
    

if __name__ == "__main__":
    main()

