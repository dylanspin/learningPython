# small learning project

import random

numOfDice = int(input("How many dice do you have?"))
numOfRols = int(input("How many times are the dice rolled?"))

# creates 2d array
allRolles = [[0 for _ in range(numOfDice)] for _ in range(numOfRols)]
rollTotal = [0] * numOfDice

# set max rolls
if(numOfDice > 40):
    numOfDice = 40

# Prints the top row dice ids
print("Dice Ids :", end=" ")  # goes to next line

# Prints the top row
for x in range(numOfDice):
    if x > 9:  # if double digit number add less space
        print(str(x) + "", end=" ")
    else:
        print(str(x) + " ", end=" ")
print("")  # goes to next line

# put into a 2d array to calculate the summary later
for x in range(numOfRols):
    for y in range(numOfDice):
        allRolles[x][y] = random.randint(0, 6)
        rollTotal[y] += allRolles[x][y]

# prints the column2
for x in range(numOfRols + 1):
    if x == numOfRols:
        print("Total    : ", end="")
    else:
        print("Rolled   :", end="")

    for y in range(numOfDice):
        if x == numOfRols:
            print(rollTotal[y], end=" ")  # prints the sum of the row
        else:
            print(" " + str(allRolles[x][y]), end=" ")  # Prints all the data from the row
    print("")  # goes to next line