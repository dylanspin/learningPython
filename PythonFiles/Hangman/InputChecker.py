# check the first char from the input 
# the input can only be a char if not ask again
# the input char needs to be capitalized so there can be no mistakes about that
# Check if the char is in the word


class checkInput:
    def checkLast(givenInput):
        if(givenInput[0].isalpha()):
            firstChar = givenInput[0].upper()
            print(firstChar)
        