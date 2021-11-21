#Elisa Turner
#November 21
#This program will play the game Vingt-et-un

def printIntro():

    #Declare variables
    name = ""

    #Intro to game
    print("Hello there, Would you like to play a game?")
    print("Before we start, whats your name?")
    name = input("Enter your name: ")
    print(f"Hello {name}! Ok, lets start")
    print(" ")


def gameMenu():

    #Declare and initialize variables
    menuChoice = 0

    menuChoice = "-1"

    #Display menu
    while menuChoice != "1" and menuChoice != "2" and menuChoice != "3":  

    
    #Display the menu and prices
        print(" Please choose from the following menu: ")
        print(f"1) See the Rules. \n2) Play Vingt-et-un. \n3) Quit")
        print("")
        #Prompt for a menu choice
        
        menuChoice = input(" Enter your choice here: ") 
        
        #Selection structure of choices
        if menuChoice == "1":
            print("+)The goal of the game is to score 21 points, or as near as possible without going over./n ")
            print("+)The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.")
            print("+)A player who totals over 21 is bust and loses the game.")
            print("+)The player whose total is nearest 21, after each player has had a turn, wins the game.")
            print("+)In the case of an equality high total, the game is tied.")
            print("+)The game is over at the end of a round when, one or both players are bust or both players choose to stay.")
            print("")
            menuChoice = "-2"
            
        elif menuChoice == "2":
            print("Heck yea, lets play!")
            gameStart()
            menuChoice= "-2"
            
        elif menuChoice == "3":
            print("Ok, lets play some other time!")
            print("")
            break
            menuChoice = "-2"

        else:
            print(" Sorry, Pleae enter a number from 1 - 3")
            print("")



def gameStart():
    #declare variables

    print("GAME START")
    print("----------------------------------------------------------------------")




#def main
    
def main():

    #Invoke printIntro function
    printIntro()

    #Invoke Game menu
    gameMenu()

    









main()


    
