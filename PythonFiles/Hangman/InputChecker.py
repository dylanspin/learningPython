# check the first char from the input 
# the input can only be a char if not ask again
# the input char needs to be capitalized so there can be no mistakes about that
# Check if the char is in the word


class checkInput:
    
    #checks the input from the user
    def checkLast(givenInput):
        if(len(givenInput) <= 0): # If the input is empty 
            print("No input given")
        if(not givenInput[0].isalpha()): # If the input is a char
            firstChar = givenInput[0].upper()
            print(firstChar)
        