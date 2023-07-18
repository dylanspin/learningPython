import random

# Hold a array of random words
# Get a random words
# return that word


class WordsController:

    allWords = [
                    "Apple","Banana","Elephant","Guitar","Chocolate","Butterfly","Laptop","Oxygen","Universe","Rainbow","Kangaroo","Lemonade","Pencil",
                    "Watermelon","Mountain","Pizza","Tornado","Telephone","Diamond","Dragonfly","Cucumber","Balloon","Giraffe","Sunflower","Telescope",
                    "Parrot","Chess","Coconut","Helicopter","Jellyfish","Lightning","Motorcycle","Octopus","Penguin","Rhinoceros","Seashell","Tomato","Umbrella",
                    "Violin","Waterfall","Zebra","Fireworks","Hotdog","Iceberg","Lighthouse","Mosquito","Nachos","Adventure","Backpack","Carnival","Dolphin",
                    "Envelope","Flamenco","Guitarist","Hummingbird","Island","Jellybean","Koala","Lavender","Monarch","Narwhal","Ostrich","Peacock","Quicksand",
                    "Raccoon","Starfish","Tortoise","Unicorn","Volleyball","Watercolor","Yacht","Bamboo","Chimpanzee","Disco","Espresso","Flamingo","Galaxy","Hyena","Ketchup",
                    "Mandarin","Ocelot","Pineapple","Quokka","Strawberry","Underwater","Vampire","Yogurt"
                ]


    def getStartWord():
        wordId = random.randint(0,len(WordsController.allWords))
        return WordsController.allWords[wordId]
    
    # convert guesing word to _ _ _ _ _ _ 
    def createGuesser(currentWord):
        newWord = ""
        for x in range(len(currentWord)):
            newWord += "_ "

        return newWord
