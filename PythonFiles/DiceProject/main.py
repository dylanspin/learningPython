import random

numOfDice = 10
numOfRols = 15

# creates 2d array
allRolles = [[int(0)] * numOfDice] * numOfRols
rollSums = [int(0)] * numOfDice

# Prints the top row dice ids
print("Dice Ids :", end = " ") # goes to next line

for x in range(numOfDice):

    if x > 9: #if double digit number add less space
        print(str(x) + "  ", end = " ") 
    else:
        print(str(x) + " ", end = " ") 

print("") # goes to next line


# put into a 2d array to calculate the summary later
for y in range(0,numOfDice):

    total = 0

    for x in range(0,numOfRols):

        allRolles[x][y] = random.randint(0,6)
        total += allRolles[x][y]

    rollSums[y] = total

# prints the colum
for x in range(0,numOfRols + 1):

    if(x == numOfRols):

        print("Sum      :", end = "")

    else :

        print("Rolled   :", end = "")

    for y in range(0,numOfDice):

        if(x == numOfRols):

            print(rollSums[y], end = " ") # prints the sum of the row

        else :

            print(" " + str(allRolles[x][y]), end = " ") # Prints all the data from the row
            
    print("") # goes to next line

# print(allRolles)