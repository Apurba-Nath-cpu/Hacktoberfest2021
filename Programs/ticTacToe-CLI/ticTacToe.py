import cmd
from pickle import FALSE
import random
import os.path

def ticTacToe():    # main function to play the game
    path=os.path.dirname(os.path.abspath(__file__))+"/doc.savedGame.txt"        
    userField, sysField, fileContents, userInpSymbol = "", "", "", ""
    gameStatus = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if(os.path.isfile(path)==True): # check whecther file exists
        with open ('doc.savedGame.txt', 'r') as fRecover:
            fileContents = fRecover.read()

    choicesPossible = "n q"
    if(fileContents != ""):     # we can resume a game only if it is saved
        # print(fileContents)
        menu = "Enter 'n' to start a new game\nEnter 'r' to resume saved game\nEnter 'q' to quit\n"
        choicesPossible += " r"
        with open('doc.savedGame.txt', 'r') as f:
            recoveredGame = f.readline()
            for pos in range(0, 8):
                gameStatus[pos] = recoveredGame[pos]

            userField = f.readline()        # reading data from the file
            userField = userField[0:len(userField)-1]
            sysField = f.readline()
            sysField = sysField[0:len(sysField)-1]
            outcome = f.readline()
            outcome = outcome[0:len(outcome)-1]
            userInpSymbol = f.readline()
            userInpSymbol = userInpSymbol

            if(outcome == "victory"):   # printing the result of last game
                print("You won the last match. You can start a new game or quit\n")
            if(outcome == "defeat"):
                print("You lost the last match. You can start a new game or quit\n") 
            if(outcome == "draw"):
                print("The last match was a draw. You can start a new game or quit\n")   
            if(outcome == "ongoing"):
                print("The last match is still ongoing. Resuming last game...\n")        

    else:
        menu= "Enter 'n' to start a new game\nEnter 'q' to quit\n"

    choice ="a"
    while(not (choicesPossible.find(choice) != -1 and len(choice) == 1)):
        choice = input(menu + "Please enter your choice: ")     # taking input
        print(choicesPossible + " " + choice)


    print("crossed\n")
    if(choice == "n"):
        resume = False
    elif(choice == "r"):    
        resume = True

    elif(choice == "q"):
        print("Exiting the game...\n")   
    if(choice == "n" or (choice == "r" and outcome.find("ongoing") != -1)):
        newGame(resume, gameStatus, userField, sysField, userInpSymbol)     # starting a game in case of valid inputs


def newGame(resume,  gameStatus, uField, sField, userInpSymbol):    # function to start a game
    gameFramework = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    userField, sysField = "", ""

    if(resume == True):     # copying data from the file if to be resumed
        gameFramework = gameStatus
        userField = uField
        sysField = sField
    
    if(resume == False):
        userInpSymbol = ""
        printGame = "(" + gameFramework[0] + ") | (" + (gameFramework[1]) + ") | (" + (gameFramework[2]) + ")\n---------------\n(" + (gameFramework[3]) + ") | (" + (gameFramework[4]) + ") | (" + (gameFramework[5]) + ")\n---------------\n(" + (gameFramework[6]) + ") | (" + (gameFramework[7]) + ") | (" + (gameFramework[8]) + ") \n"
        print("\n" + printGame)
        while(not (userInpSymbol == "1" or userInpSymbol == "2")):
            userInpSymbol = input("Press 1 to select O\nPress 2 to select X\n")
            if(not (userInpSymbol == "1" or userInpSymbol == "2")):
                print("Please enter a valid input!\n")

        if(userInpSymbol == "1"):
            userInpSymbol = "O"
            sysInpSymbol = "X"
        else:
            userInpSymbol = "X"  
            sysInpSymbol = "O" 
    else:
        print("Your symbol is " + userInpSymbol)    


    userMove(gameFramework, userInpSymbol, userField, sysField)

def userMove(gameStatus, userInpSymbol, userField, sysField):   # function to take user input
    victory, ongoing = "victory", "ongoing"
    currentGame = "(" + gameStatus[0] + ") | (" + (gameStatus[1]) + ") | (" + (gameStatus[2]) + ")\n---------------\n(" + (gameStatus[3]) + ") | (" + (gameStatus[4]) + ") | (" + (gameStatus[5]) + ")\n---------------\n(" + (gameStatus[6]) + ") | (" + (gameStatus[7]) + ") | (" + (gameStatus[8]) + ") \n"
    
    if(checkVictory(userField)):        # check if player is a winner
        print("Congrats! You won the game. The final game status looks like:\n" + currentGame)
        quitGame(gameStatus, userField, sysField, userInpSymbol, victory)

    userMoveIndex = "a"
    allPossibilities = "1 2 3 4 5 6 7 8 9"
    print("Current game status:\n" + currentGame)
    while((not userMoveIndex.isdigit())):
        userMoveIndex = input("Enter your move in the format <position> Eg. 7, or enter 'q' to quit and save the game: ")   # takes user input
        if(userMoveIndex.isdigit()):
            if(userField.find(userMoveIndex) != -1 or sysField.find(userMoveIndex) != -1 or allPossibilities.find(userMoveIndex) == -1):
                print("This position is not vacant! ")
                userMoveIndex ="a"
        else:
            if(userMoveIndex.lower() != "q"):
                print("Please enter a valid index\n\n")
            else:
                break    

    if(userMoveIndex == "q"):
        quitGame(gameStatus, userField, sysField, userInpSymbol, ongoing)

    userField = userField + userMoveIndex
    printModifiedGame = "(" + gameStatus[0] + ") | (" + (gameStatus[1]) + ") | (" + (gameStatus[2]) + ")\n---------------\n(" + (gameStatus[3]) + ") | (" + (gameStatus[4]) + ") | (" + (gameStatus[5]) + ")\n---------------\n(" + (gameStatus[6]) + ") | (" + (gameStatus[7]) + ") | (" + (gameStatus[8]) + ") \n"
    printModifiedGame = printModifiedGame.replace(userMoveIndex, userInpSymbol)
    modifiedGame = gameStatus
    modifiedGame[int(userMoveIndex) - 1] = userInpSymbol

    if(checkVictory(userField)):    # check if the user won
        print("Congrats! You won the game. The final game status looks like:\n" + printModifiedGame)
        quitGame(modifiedGame, userField, sysField, userInpSymbol, victory)
    else:
        sysMove(modifiedGame, userInpSymbol, userMoveIndex, userField, sysField)

def sysMove(gameStatus, userInpSymbol, userMoveIndex, userField, sysField):     # function to make the system make a move
    if(userInpSymbol == "O"):
        sysInpSymbol = "X"
    else:
        sysInpSymbol = "O"

    currentGame = "(" + gameStatus[0] + ") | (" + (gameStatus[1]) + ") | (" + (gameStatus[2]) + ")\n---------------\n(" + (gameStatus[3]) + ") | (" + (gameStatus[4]) + ") | (" + (gameStatus[5]) + ")\n---------------\n(" + (gameStatus[6]) + ") | (" + (gameStatus[7]) + ") | (" + (gameStatus[8]) + ") \n"
    conditionForVictory = ["123", "456", "789", "147", "258", "369", "159", "357"]
    draw, defeat = "draw", "defeat"

    if(len(userField) + len(sysField) == 9):    # check if grid is full
        print("Game is a draw!\n")
        quitGame(gameStatus, userField, sysField, userInpSymbol, draw)             

    sysMoveIndex = ""
    modifiedGame = ""
    for indexWin in conditionForVictory:
        if(sysField.find(indexWin[0]) != -1 and sysField.find(indexWin[1]) != -1 and userField.find(indexWin[2]) == -1):
            sysMoveIndex = indexWin[2]
        if(sysField.find(indexWin[1]) != -1 and sysField.find(indexWin[2]) != -1 and userField.find(indexWin[0]) == -1):  
            sysMoveIndex = indexWin[0]
        if(sysField.find(indexWin[2]) != -1 and sysField.find(indexWin[0]) != -1 and userField.find(indexWin[1]) == -1):     
            sysMoveIndex = indexWin[1]

    if(sysMoveIndex != ""):     # check if the system can win in this move
        sysField = sysField + sysMoveIndex
        currentGame = currentGame.replace(sysMoveIndex, sysInpSymbol)
        modifiedGame = gameStatus
        modifiedGame[int(sysMoveIndex) - 1] = sysInpSymbol

        print("Oops! Better luck next time. The final game status looks like:\n" + currentGame)
        quitGame(modifiedGame, userField, sysField, userInpSymbol, defeat)

    for indexWin in conditionForVictory:
        if(userField.find(indexWin[0]) != -1 and userField.find(indexWin[1]) != -1 and sysField.find(indexWin[2]) == -1):
            sysMoveIndex = indexWin[2]
        if(userField.find(indexWin[1]) != -1 and userField.find(indexWin[2]) != -1 and sysField.find(indexWin[0]) == -1):  
            sysMoveIndex = indexWin[0]
        if(userField.find(indexWin[2]) != -1 and userField.find(indexWin[0]) != -1 and sysField.find(indexWin[1]) == -1):     
            sysMoveIndex = indexWin[1]    

    if(sysMoveIndex != ""):     # prevent the user from winning in the next move
        sysField = sysField + sysMoveIndex
        currentGame = currentGame.replace(sysMoveIndex, sysInpSymbol)
        modifiedGame = gameStatus
        modifiedGame[int(sysMoveIndex) - 1] = sysInpSymbol

    while(sysMoveIndex == ""):      # or else make a random move
        possibleMove = str(random.randrange(1,10,1))

        if(userField.find(possibleMove) == -1 and sysField.find(possibleMove) == -1):
            sysMoveIndex = possibleMove
            sysField = sysField + sysMoveIndex
            currentGame = currentGame.replace(sysMoveIndex, sysInpSymbol)
            modifiedGame = gameStatus
            modifiedGame[int(sysMoveIndex) - 1] = sysInpSymbol   
            print("Your move is: " + userMoveIndex + "\nSystem's move is: " + sysMoveIndex) 

    userMove(modifiedGame, userInpSymbol, userField, sysField)
        
def checkVictory(field):    # function to check the victory of a party
    conditionForVictory = ["123", "456", "789", "147", "258", "369", "159", "357"]
    for indexWin in conditionForVictory:
        if(field.find(indexWin[0]) != -1 and field.find(indexWin[1]) != -1 and field.find(indexWin[2]) != -1):
            return True
    return False 

def quitGame(gameStatus, userField, sysField, userInpSymbol, outcome):      # function to quit and save the game
    savedGame = ""
    for pos in gameStatus:
        savedGame = savedGame + pos
    path=os.path.dirname(os.path.abspath(__file__))+"/doc.savedGame.txt"        
    print("Game status is saved in " + path + "\n")
    with open('doc.savedGame.txt', 'w') as f:
        f.write(savedGame + "\n") 
        f.write(userField + "\n")
        f.write(sysField + "\n")
        f.write(outcome + "\n")
        f.write(userInpSymbol)  
    exit(0)           

ticTacToe()