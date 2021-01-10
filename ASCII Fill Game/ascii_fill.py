#Name: Eric Tran
#Student Number: 101154728
def readLevel(LevelNumber):
    try:
        #Tries to open the file
        if LevelNumber == 1:
            f = open("./levels/ascii_level1.txt","r")
        if LevelNumber == 2:
            f = open("./levels/ascii_level2.txt","r")
        if LevelNumber == 3:
            f = open("./levels/ascii_level3.txt","r")
        if LevelNumber == 4:
            f = open("./levels/ascii_level4.txt","r")
        if LevelNumber == 5:
            f = open("./levels/ascii_level5.txt","r")  
    except:
        print("ERROR! FILE DOES NOT EXIST")
        exit()
    LevelList = []
    i=0
    #Puts the values in the text file into a 2D list
    for line in f:
        LevelList.append([])
        IndividualLine = line.strip()
        for Character in IndividualLine:
            LevelList[i].append(Character)
        i += 1
    f.close()
    return LevelList
def displayBoard(Level):
    row = ''
    boarder = "   "
    CharacterIndex = 0
    rowNum = 0
    #Column labels // border
    row += "   "
    for i in range(len(Level[0])):
        if i < 10:
            row += str(i)
        else:
            if rowNum > 9:
                rowNum = 0
            row += str(rowNum)
        boarder += "-"
        rowNum += 1
    #prints out the labels
    print(row)
    print(boarder)
    row = ''
    #For all remaining rows
    for j in range(len(Level)):
        #The row labels
        if j == 0:
            row += "00" + "|"
        elif j < 10:
            row += "0" + str(j)+ "|"
        else:
            row += str(j)+ "|"
        #prints the characters
        for character in Level[j]:
            row += character
            CharacterIndex += 1
        print(row)
        row = ''
def getUserAction(BoardWidth,BoardLength):
    symbol= ''
    row=column=-1
    Ouput = []
    #Asks for the symbol // Will loop until a valid symbol is entered
    while symbol not in {'&','@','#','%'}:
        symbol = input("Enter a symbol: ")
        if symbol not in {'&','@','#','%'}:
            print("Enter a valid symbol")
    #For row //Loops until the choice is in range
    while (0<=row<=BoardWidth) == False:
        try:
            row = int(input(f"Select a row: [0,{BoardWidth}]: ")) 
            if (0<=row<=BoardWidth) == False:
                print("Enter a valid row")
        except:
            print("Enter a valid row")
    #For column //Loops until the choice is in range
    while (0<=column<=BoardLength) == False:
        try:
            column = int(input(f"Select a column: [0,{BoardLength}]: ")) 
            if (0<=column<=BoardLength) == False:
                print("Enter a valid column")
        except:
            print("Enter a valid column")
    #Adds the necessary values 
    Ouput.extend([symbol,row,column])     
    return Ouput
def fill(Level,ReplacingSymbol,TargetSymbol,RowIndex,ColumnIndex):
    #If symbol chosen is the same as the symbol picked on the grid it will not replace anything
    if TargetSymbol == ReplacingSymbol:
        return
    #If the symbol at the given location is not the symbol we want to replace then do nothing
    if Level[RowIndex][ColumnIndex] != TargetSymbol:
        return
    if TargetSymbol == None:
        TargetSymbol = Level[RowIndex][ColumnIndex]
        
    Level[RowIndex][ColumnIndex] = ReplacingSymbol
    #The adjacent symbols (Up, Down, Left, Right)
    if ColumnIndex > 0:
        fill(Level,ReplacingSymbol,TargetSymbol,RowIndex,ColumnIndex-1)
    if RowIndex > 0:
        fill(Level,ReplacingSymbol,TargetSymbol,RowIndex-1,ColumnIndex)
    if ColumnIndex < len(Level[0])-1:
        fill(Level,ReplacingSymbol,TargetSymbol,RowIndex,ColumnIndex+1)
    if RowIndex < len(Level)-1:
        fill(Level,ReplacingSymbol,TargetSymbol,RowIndex+1,ColumnIndex)
def checkBoard(level):
    #First row
    Temp = level[0]  
    #Runs through all rows of the level
    for i in range (1,len(level)):
        '''
        Runs through rows 1-the end. If at any point the a row is not equivalent to the first row (temp) then it will return False.
        If the for loop is able to completely run through all rows in the level it can be determined that all rows in the level are the same.
        '''
        if Temp == level[i]:
            continue
        else:
            return False
    return True      
def main():
    #Sets the user's moves for each round and the total moves everytime the game is started
    userMoves = 0
    moveTotal = 0
    for i in range (1,6): #Will go through the 5 levels
        fullBoard = False
        #Sets the level according to the i value
        Level = readLevel(i) 
        #Displays the board
        displayBoard(Level)
        while fullBoard == False:
            #Gets user input
            #[symbol,row,column]
            UserOuput = getUserAction(len(Level)-1,len(Level[0])-1) 
                
            #Breaks down the list that was recieved from the above function. 
            #Gets the target symbol using the row and column index
            RowIndex = UserOuput[1]
            ColumnIndex = UserOuput[2]
            ReplacingSymbol= UserOuput[0]
            TargetSymbol = Level[RowIndex][ColumnIndex]
                
            #Fills the list
            fill(Level,ReplacingSymbol,TargetSymbol,RowIndex,ColumnIndex)
            displayBoard(Level)
            userMoves += 1
            #Checks if the board is complete
            fullBoard = checkBoard(Level)
            if fullBoard == True:
                print(f"Level {i} completed in {userMoves} moves!")
                print(" ")
                moveTotal += userMoves
                userMoves = 0

    print("You win! Thanks for playing!")
    print(f"Total moves: {moveTotal}")
    UserInput = input("Would you like to play again? (y/n): ")  
    #Loops until either 'y' or 'n' is inputted
    while True:
        if UserInput in {'n','y'}:
            break
        print("Invalid response. Please enter 'y' or 'n'.")
        UserInput = input("Would you like to play again? (y/n): ")
    if UserInput == 'y':
        #Resets the game by calling the main function again
        main()
    if UserInput == 'n':
        None
main()