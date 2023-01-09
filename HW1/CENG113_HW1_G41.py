import random

#these three variables will save the total points the player earns throughout the game
totalBunco = 0
totalMiniBunco = 0
totalDieMatchedRound = 0

#these nine variables will save the points per roll
#these will be used to check whether points were earned during a roll
#they will be added to the total points after each round to keep the total score
#after each round, they will be reset in order to be used for the next round

bunco1 = 0
miniBunco1 = 0
dieMatchedRound1 = 0

#variables for second roll
bunco2 = 0
miniBunco2 = 0
dieMatchedRound2 = 0

#variables for third roll
bunco3 = 0
miniBunco3 = 0
dieMatchedRound3 = 0

roundNumber = 1 #this variable will be used in order to check whether there is a matching die with round number

#throwing the dice
input("Press enter to roll the dices.") #Make the user feel like they are rolling the dice by making an input.Just for more interactivity.
die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("You are on the first round!")
print("This is your first roll")
print("Your dice are rolled as: ",die1 ,die2 ,die3)

if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber: #check for a bunco, criterion a
    totalBunco = totalBunco + 1
    bunco1 = 1
    print("BUNCO!! Congratulations!")
elif die1 == die2 and die2 == die3: #check for a mini-bunco, criterion b
    totalMiniBunco = totalMiniBunco + 1
    miniBunco1 = 1
    print("Mini-BUNCO! Congratulations!")
elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber: #check if any die matches the round number, criterion c
    if die1 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die2 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die3 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0: #check if any points were earned throughout the roll
    print("You have gotten " + str((bunco1) * 21 + (miniBunco1) * 5 + dieMatchedRound1) + " points on this roll")
else:
    print("You earned no points on this roll")

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0: #check if any points were earned during the previous roll in order to roll again
    input("Press enter to roll the dices again.")
    print("____________________________________") #Print underscore to differ every dice roll from each other just to make UI more clear
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your second roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco2 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco2 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
    if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
        print("You have gotten " + str((bunco2) * 21 + (miniBunco2) * 5 + dieMatchedRound2) + " points on this roll")
    else:
        print("You earned no points on this roll")

if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0: #check if any points were earned during the previous roll in order to roll again
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your third roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco3 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco3 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
    if bunco3 > 0 or miniBunco3 > 0 or dieMatchedRound3 > 0:
        print("You have gotten " + str((bunco3) * 21 + (miniBunco3) * 5 + dieMatchedRound3) + " points on this roll")
    else:
        print("You earned no points on this roll")


print("First round ended!")
print("You have gotten " + str((bunco1 + bunco2 + bunco3) * 21 + (miniBunco1 + miniBunco2 + miniBunco3) * 5 + dieMatchedRound1 + dieMatchedRound2 + dieMatchedRound3) + " points on this round")
print("Your total points: " ,totalBunco * 21 + totalMiniBunco * 5 + totalDieMatchedRound)

#resetting the roll variables in order to use in the next round
bunco1 = 0
miniBunco1 = 0
dieMatchedRound1 = 0

bunco2 = 0
miniBunco2 = 0
dieMatchedRound2 = 0

bunco3 = 0
miniBunco3 = 0
dieMatchedRound3 = 0

roundNumber = 2
input("Press enter to roll the dices again.")
print("____________________________________")
die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("You are on the second round!")
print("This is your first roll")
print("Your dice are rolled as: ",die1 ,die2 ,die3)

if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
    totalBunco = totalBunco + 1
    bunco1 = 1
    print("BUNCO!! Congratulations!")
elif die1 == die2 and die2 == die3:
    totalMiniBunco = totalMiniBunco + 1
    miniBunco1 = 1
    print("Mini-BUNCO! Congratulations!")
elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
    if die1 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die2 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die3 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    print("You have gotten " + str((bunco1) * 21 + (miniBunco1) * 5 + dieMatchedRound1) + " points on this roll")
else:
    print("You earned no points on this roll")

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your second roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco2 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco2 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
    if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
        print("You have gotten " + str((bunco2) * 21 + (miniBunco2) * 5 + dieMatchedRound2) + " points on this roll")
    else:
        print("You earned no points on this roll")

if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your third roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco3 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco3 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
    if bunco3 > 0 or miniBunco3 > 0 or dieMatchedRound3 > 0:
        print("You have gotten " + str((bunco3) * 21 + (miniBunco3) * 5 + dieMatchedRound3) + " points on this roll")
    else:
        print("You earned no points on this roll")


print("Second round ended!")
print("You have gotten " + str((bunco1 + bunco2 + bunco3) * 21 + (miniBunco1 + miniBunco2 + miniBunco3) * 5 + dieMatchedRound1 + dieMatchedRound2 + dieMatchedRound3) + " points on this round")
print("Your total points: " ,totalBunco * 21 + totalMiniBunco * 5 + totalDieMatchedRound)

bunco1 = 0
miniBunco1 = 0
dieMatchedRound1 = 0

bunco2 = 0
miniBunco2 = 0
dieMatchedRound2 = 0

bunco3 = 0
miniBunco3 = 0
dieMatchedRound3 = 0

roundNumber = 3
input("Press enter to roll the dices again.")
print("____________________________________")
die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("You are on the third round!")
print("This is your first roll")
print("Your dice are rolled as: ",die1 ,die2 ,die3)

if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
    totalBunco = totalBunco + 1
    bunco1 = 1
    print("BUNCO!! Congratulations!")
elif die1 == die2 and die2 == die3:
    totalMiniBunco = totalMiniBunco + 1
    miniBunco1 = 1
    print("Mini-BUNCO! Congratulations!")
elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
    if die1 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die2 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die3 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    print("You have gotten " + str((bunco1) * 21 + (miniBunco1) * 5 + dieMatchedRound1) + " points on this roll")
else:
    print("You earned no points on this roll")

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your second roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco2 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco2 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
    if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
        print("You have gotten " + str((bunco2) * 21 + (miniBunco2) * 5 + dieMatchedRound2) + " points on this roll")
    else:
        print("You earned no points on this roll")

if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your third roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco3 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco3 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
    if bunco3 > 0 or miniBunco3 > 0 or dieMatchedRound3 > 0:
        print("You have gotten " + str((bunco3) * 21 + (miniBunco3) * 5 + dieMatchedRound3) + " points on this roll")
    else:
        print("You earned no points on this roll")


print("Third round ended!")
print("You have gotten " + str((bunco1 + bunco2 + bunco3) * 21 + (miniBunco1 + miniBunco2 + miniBunco3) * 5 + dieMatchedRound1 + dieMatchedRound2 + dieMatchedRound3) + " points on this round")
print("Your total points: " ,totalBunco * 21 + totalMiniBunco * 5 + totalDieMatchedRound)

bunco1 = 0
miniBunco1 = 0
dieMatchedRound1 = 0

bunco2 = 0
miniBunco2 = 0
dieMatchedRound2 = 0

bunco3 = 0
miniBunco3 = 0
dieMatchedRound3 = 0

roundNumber = 4
input("Press enter to roll the dices again.")
print("____________________________________")
die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("You are on the fourth round!")
print("This is your first roll")
print("Your dice are rolled as: ",die1 ,die2 ,die3)

if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
    totalBunco = totalBunco + 1
    bunco1 = 1
    print("BUNCO!! Congratulations!")
elif die1 == die2 and die2 == die3:
    totalMiniBunco = totalMiniBunco + 1
    miniBunco1 = 1
    print("Mini-BUNCO! Congratulations!")
elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
    if die1 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die2 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die3 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    print("You have gotten " + str((bunco1) * 21 + (miniBunco1) * 5 + dieMatchedRound1) + " points on this roll")
else:
    print("You earned no points on this roll")

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your second roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco2 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco2 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
    if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
        print("You have gotten " + str((bunco2) * 21 + (miniBunco2) * 5 + dieMatchedRound2) + " points on this roll")
    else:
        print("You earned no points on this roll")

if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your third roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco3 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco3 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
    if bunco3 > 0 or miniBunco3 > 0 or dieMatchedRound3 > 0:
        print("You have gotten " + str((bunco3) * 21 + (miniBunco3) * 5 + dieMatchedRound3) + " points on this roll")
    else:
        print("You earned no points on this roll")


print("Fourth round ended!")
print("You have gotten " + str((bunco1 + bunco2 + bunco3) * 21 + (miniBunco1 + miniBunco2 + miniBunco3) * 5 + dieMatchedRound1 + dieMatchedRound2 + dieMatchedRound3) + " points on this round")
print("Your total points: " ,totalBunco * 21 + totalMiniBunco * 5 + totalDieMatchedRound)

bunco1 = 0
miniBunco1 = 0
dieMatchedRound1 = 0

bunco2 = 0
miniBunco2 = 0
dieMatchedRound2 = 0

bunco3 = 0
miniBunco3 = 0
dieMatchedRound3 = 0

roundNumber = 5
input("Press enter to roll the dices again.")
print("____________________________________")
die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("You are on the fifth round!")
print("This is your first roll")
print("Your dice are rolled as: ",die1 ,die2 ,die3)

if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
    totalBunco = totalBunco + 1
    bunco1 = 1
    print("BUNCO!! Congratulations!")
elif die1 == die2 and die2 == die3:
    totalMiniBunco = totalMiniBunco + 1
    miniBunco1 = 1
    print("Mini-BUNCO! Congratulations!")
elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
    if die1 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die2 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die3 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    print("You have gotten " + str((bunco1) * 21 + (miniBunco1) * 5 + dieMatchedRound1) + " points on this roll")
else:
    print("You earned no points on this roll")

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your second roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco2 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco2 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
    if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
        print("You have gotten " + str((bunco2) * 21 + (miniBunco2) * 5 + dieMatchedRound2) + " points on this roll")
    else:
        print("You earned no points on this roll")

if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your third roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco3 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco3 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
    if bunco3 > 0 or miniBunco3 > 0 or dieMatchedRound3 > 0:
        print("You have gotten " + str((bunco3) * 21 + (miniBunco3) * 5 + dieMatchedRound3) + " points on this roll")
    else:
        print("You earned no points on this roll")


print("Fifth round ended!")
print("You have gotten " + str((bunco1 + bunco2 + bunco3) * 21 + (miniBunco1 + miniBunco2 + miniBunco3) * 5 + dieMatchedRound1 + dieMatchedRound2 + dieMatchedRound3) + " points on this round")
print("Your total points: " ,totalBunco * 21 + totalMiniBunco * 5 + totalDieMatchedRound)

bunco1 = 0
miniBunco1 = 0
dieMatchedRound1 = 0

bunco2 = 0
miniBunco2 = 0
dieMatchedRound2 = 0

bunco3 = 0
miniBunco3 = 0
dieMatchedRound3 = 0

roundNumber = 6
input("Press enter to roll the dices again.")
print("____________________________________")
die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("You are on the sixth and last round!")
print("This is your first roll")
print("Your dice are rolled as: ",die1 ,die2 ,die3)

if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
    totalBunco = totalBunco + 1
    bunco1 = 1
    print("BUNCO!! Congratulations!")
elif die1 == die2 and die2 == die3:
    totalMiniBunco = totalMiniBunco + 1
    miniBunco1 = 1
    print("Mini-BUNCO! Congratulations!")
elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
    if die1 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die2 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1
    if die3 == roundNumber:
        totalDieMatchedRound = totalDieMatchedRound + 1
        dieMatchedRound1 = dieMatchedRound1 + 1

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    print("You have gotten " + str((bunco1) * 21 + (miniBunco1) * 5 + dieMatchedRound1) + " points on this roll")
else:
    print("You earned no points on this roll")

if bunco1 > 0 or miniBunco1 > 0 or dieMatchedRound1 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your second roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco2 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco2 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound2 = dieMatchedRound2 + 1
    if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
        print("You have gotten " + str((bunco2) * 21 + (miniBunco2) * 5 + dieMatchedRound2) + " points on this roll")
    else:
        print("You earned no points on this roll")

if bunco2 > 0 or miniBunco2 > 0 or dieMatchedRound2 > 0:
    input("Press enter to roll the dices again.")
    print("____________________________________")
    die1, die2, die3 = random.randint(1,6), random.randint(1,6), random.randint(1,6)

    print("This is your third roll")
    print("Your dice are rolled as: ",die1 ,die2 ,die3)

    if die1 == roundNumber and die2 == roundNumber and die3 == roundNumber:
        totalBunco = totalBunco + 1
        bunco3 = 1
        print("BUNCO!! Congratulations!")
    elif die1 == die2 and die2 == die3:
        totalMiniBunco = totalMiniBunco + 1
        miniBunco3 = 1
        print("Mini-BUNCO! Congratulations!")
    elif die1 == roundNumber or die2 == roundNumber or die3 == roundNumber:
        if die1 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die2 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
        if die3 == roundNumber:
            totalDieMatchedRound = totalDieMatchedRound + 1
            dieMatchedRound3 = dieMatchedRound3 + 1
    if bunco3 > 0 or miniBunco3 > 0 or dieMatchedRound3 > 0:
        print("You have gotten " + str((bunco3) * 21 + (miniBunco3) * 5 + dieMatchedRound3) + " points on this roll")
    else:
        print("You earned no points on this roll")

print("Sixth and last round ended!")
print("You have gotten " + str((bunco1 + bunco2 + bunco3) * 21 + (miniBunco1 + miniBunco2 + miniBunco3) * 5 + dieMatchedRound1 + dieMatchedRound2 + dieMatchedRound3) + " points on this round")
input("Press enter to see the results.")
print("____________________________________")
print("Your total points at the end of the game: " ,totalBunco * 21 + totalMiniBunco * 5 + totalDieMatchedRound)
print("Total BUNCO count: ",totalBunco)
print("Total mini-BUNCO count: ",totalMiniBunco)