# S10227737K
# Nur Muhammad Bin Ismail PO1
# 9/8/21

import random

#this will display the main menu
def mainMenu():
    print("Welcome, mayor of Simp City!")
    print("----------------------------")
    print("1. Start new game")
    print("2. Load saved game")
    print()
    print("0. Exit")

mainMenu()
menu_option = int(input("Your choice? "))



# this function will print out the map
def printBoard():
    print("     A     B     C     D")
    print(" ", "+-----+-----+-----+-----+")
    for row in range(1, 5):
        print(" {}".format(row), end="")
        for column in range(1, 5):
            print("| {:3} ".format(board[row][column]), end="")
        print("|")
        print(" ", "+-----+-----+-----+-----+")


#this is the scoring system for HOUSE
def scoreHSE():
    global totalHSE
    totalHSE = 0            #totalHSE is the scoring
    hseList = []
    hsePos = []
    for column in range(len(board)):
        for row in range(len(board)):
            if board[row][column] == 'HSE':
                hsePos.append([row, column])

    for y in hsePos:
        if board[y[0] + 1][y[1]] == 'FAC' or board[y[0]][y[1] + 1] == 'FAC' or board[y[0] - 1][y[1]] == 'FAC' or \
                board[y[0]][y[1] - 1] == 'FAC':  #if the position it is in is a FAC, it gives 1 points
            totalHSE = 1
        else:
            if board[y[0] + 1][y[1]] == 'SHP':  #from line 50 - 57, this checks whether the position is a SHP, if it is, it gives 1 points
                totalHSE += 1
            if board[y[0]][y[1] + 1] == 'SHP':
                totalHSE += 1
            if board[y[0] - 1][y[1]] == 'SHP':
                totalHSE+= 1
            if board[y[0]][y[1] - 1] == 'SHP':
                totalHSE += 1
            if board[y[0] + 1][y[1]] == 'HSE': #from line 58 - 64, this checks whether the position is a HSE, if it is, it gives 1 points
                totalHSE += 1
            if board[y[0]][y[1] + 1] == 'HSE':
                totalHSE += 1
            if board[y[0] - 1][y[1]] == 'HSE':
                totalHSE += 1
            if board[y[0]][y[1] - 1] == 'HSE':
                totalHSE += 1
            if board[y[0] + 1][y[1]] == 'BCH': #from line 66 - 72, this checks whether the position is a BCH, if it is, it gives 2 points
                totalHSE += 2
            if board[y[0]][y[1] + 1] == 'BCH':
                totalHSE += 2
            if board[y[0] - 1][y[1]] == 'BCH':
                totalHSE += 2
            if board[y[0]][y[1] - 1] == 'BCH':
                totalHSE += 2
        hseList.append(totalHSE)
        totalHSE -= totalHSE
    for i in hseList:
        totalHSE += i
    hsePts = ' + '.join(str(x) for x in hseList)        # this will add up the score for house
    if totalHSE != 0:
        print('HSE:', hsePts + ' = ', totalHSE)
    elif totalHSE == 0:
        print()

    return totalHSE

#this is the scoring system for FACTORY
def scoreFAC():
    global totalFAC
    count = 0
    totalFAC = 0            #totalFAC represents the number of points
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 'FAC':
                count += 1
    if count <= 4:              #count represent the number of FAC
        if count == 1:
            totalFAC = 1        #if there is 1 FAC, it gives 1 point
        elif count == 2:
            totalFAC = 4       #if there is 2 FAC, it gives 4 point
        elif count == 3:
            totalFAC = 9       #if there is 3 FAC, it gives 4 point
        elif count == 4:
            totalFAC = 16      #if there is 4 FAC, it gives 16 point
    elif count > 4:
        totalFAC = 16 + (count - 4)     #if there is more than 4 FAC, it will first give 16 points, then add the extra number of FAC minus 4

    if count == 1:
        print('{}{}{}{}{}'.format('FAC', ': ', '1', ' = ', totalFAC))                 #line 108 - 116 prints out the scoring for FAC, if 1 FAC, it will print out 1 etc
    elif count == 2:
        print('{}{}{}{}{}{}'.format('FAC', ': ', '2', ' + 2', ' = ', totalFAC))
    elif count == 3:
        print('{}{}{}{}{}{}'.format('FAC', ': ', '3', ' + 3' * (count - 1), ' = ', totalFAC))
    elif count == 4:
        print('{}{}{}{}{}{}'.format('FAC', ': ', '4', ' + 4' * (count - 1), ' = ', totalFAC))
    elif count > 4:
        print('{}{}{}{}{}{}{}'.format('FAC', ': ', '4', ' + 4' * 3, ' + 1' * (count - 4), ' = ', totalFAC))
    return totalFAC


#this is the scoring for the SHOP
def scoreSHP():
    global totalSHP
    totalSHP = 0        #totalSHP represents the number of points
    shpList = []
    shpPos = []         #checks position of SHP
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 'SHP':
                shpPos.append([row, column])
    for y in shpPos:
        if board[y[0] + 1][y[1]] == 'FAC' or board[y[0] - 1][y[1]] == 'FAC' or board[y[0]][y[1] + 1] == 'FAC' or \
                board[y[0]][y[1] - 1] == 'FAC': #this checks the board whether if it is a FAC, if it is then 1 points
            totalSHP += 1
        if board[y[0] + 1][y[1]] == 'HSE' or board[y[0] - 1][y[1]] == 'HSE' or board[y[0]][y[1] + 1] == 'HSE' or \
                board[y[0]][y[1] - 1] == 'HSE': #this checks the board whether if it is a HSE, if it is then 1 points
            totalSHP += 1
        if board[y[0] + 1][y[1]] == 'BCH' or board[y[0] - 1][y[1]] == 'BCH' or board[y[0]][y[1] + 1] == 'BCH' or \
                board[y[0]][y[1] - 1] == 'BCH': #this checks the board whether if it is a BCH, if it is then 1 points
            totalSHP += 1
        if board[y[0] + 1][y[1]] == 'SHP' or board[y[0] - 1][y[1]] == 'SHP' or board[y[0]][y[1] + 1] == 'SHP' or \
                board[y[0]][y[1] - 1] == 'SHP': #this checks the board whether if it is a SHP, if it is then 1 points
            totalSHP += 1
        if board[y[0] + 1][y[1]] == 'HWY' or board[y[0] - 1][y[1]] == 'HWY' or board[y[0]][y[1] + 1] == 'HWY' or \
                board[y[0]][y[1] - 1] == 'HWY': #this checks the board whether if it is a HWY, if it is then 1 points
            totalSHP += 1
        shpList.append(totalSHP)
        totalSHP -= totalSHP

    for i in shpList:
        totalSHP += i
    shpPts = ' + '.join(str(x) for x in shpList)        #this will add up the score for SHP
    if totalSHP != 0:
        print('SHP:', shpPts + ' = ', totalSHP)
    elif totalSHP == 0:
        print()
    return totalSHP

#this is the scoring for the HIGHWAY
def scoreHWY():
    global totalHWY
    hwyList = []
    count = 0                          #count represents the number of HWY
    totalHWY = 0                       #totalHWY represents the points
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 'HWY':
                count = 1
                while board[row][column + 1] == 'HWY' and column < 5:
                    count += 1
                    board[row][column + 1] = 'HWY'
                    column += 1
                hwyList.append(count)
                totalHWY += count
            elif board[row][column] == 'HWY':
                board[row][column] = 'HWY'
                count = hwyList[-1]
                hwyList.append(count)
                totalHWY += count

    print('HWY: ', end='')
    for x in range(len(hwyList)):
        if x + 1 == len(hwyList):
            print(hwyList[x], end=' = ')        #this will add up the score for HWY
        else:
            print(hwyList[x], end=' + ')

    print(totalHWY)
    return totalHWY



#this is the scoring for the BEACH
def scoreBCH():
    global totalBCH
    beach1 = 0      #this represents the number of beach in  A/D
    beach2 = 0      #this represents the number of beach in  B/C
    totalBCH = 0    #represents the points for BCH
    for row in range(len(board)):
        if board[row][1] == 'BCH' or board[row][4] == 'BCH':
            beach1 += 1
            totalBCH += 3       #if it is in row 1/4 aka A/D on the board, gives 3 pts
        elif board[row][2] == 'BCH' or board[row][3] == 'BCH':
            beach2 += 1         #if it is in row 2/3 aka B/C on the board, gives 1 pts
            totalBCH += 1

    if beach1 >= 1 and beach2 >= 1:
        print('{}{}{}{}{}{}{}{}'.format('BCH', ': ', '3' , ' + 3' * (beach1 - 1),' + ','1',' + 1' * (beach2 - 1),' = ', totalBCH))
    elif beach1 >= 1 and beach2 == 0:
        print('{}{}{}{}{}{}'.format('BCH', ': ', '3' , ' + 3' * (beach1 - 1),' = ', totalBCH))
    elif beach1 == 0 and beach2 >= 1:
        print('{}{}{}{}{}{}'.format('BCH', ': ', '1',' + 1' * (beach2 - 1),' = ', totalBCH))
    else:
        print()
    return totalBCH



#this function saves the current game state and saves it in the directory
def save_game(board, option1, option2, turn, building):
    path = 'C:\\Users\\dexal\\PycharmProjects\\NP\\'
    file = open(path + 'savegame.txt', 'w')
    savegameList = [board, option1, option2, turn, building]
    file.write(str(savegameList))
    file.close()
    print('Game Saved!')





while True:
    #this loads the save state and u can continue playing from ther
    if menu_option == 2:
        saveList = []
        path = 'C:\\Users\\dexal\\PycharmProjects\\NP\\'
        file = open(path + 'savegame.txt', 'r')
        for line in file:
            saveList = line
        file.close()
        saveList = eval(saveList)
        board = saveList[0]
        option1 = saveList[1]
        option2 = saveList[2]
        turn = saveList[3]
        building = saveList[4]
        if menu_option != 2:
            print('Invalid option')
    #if user decides to exit the game this choice is available to him
    elif menu_option == 0:
            break

    #this is the start of a new game
    elif menu_option == 1:
        board = [["   ", "   ", "   ", "   ", "   ", "   "],
                 ["   ", "   ", "   ", "   ", "   ", "   "],
                 ["   ", "   ", "   ", "   ", "   ", "   "],
                 ["   ", "   ", "   ", "   ", "   ", "   "],
                 ["   ", "   ", "   ", "   ", "   ", "   "],
                 ["   ", "   ", "   ", "   ", "   ", "   "],
                 ]
        turn = 1
        building = [["HSE", 8], ["FAC", 8], ["SHP", 8], ["HWY", 8], ["BCH", 8]]
        option1 = building[random.randint(0, 4)][0]          # this gives a random option of building from the list
        option2 = building[random.randint(0, 4)][0]          # this gives a random option of building from the list

    #the game will continue on till turn 16
    while turn <= 16:
        print('Turn ', turn)
        printBoard()
        option1 = building[random.randint(0, 4)][0]         # this gives a random option of building from the list
        option2 = building[random.randint(0, 4)][0]         # this gives a random option of building from the list
        print("1. Build a", option1)
        print("2. Build a", option2)
        print("3. See remaining buildings")
        print("4. See current score")
        print()
        print('5. Save game')
        print("0. Exit to main menu")

        playerChoice = int(input("Your choice? "))
        if playerChoice == 0:                               # if user chooses this option, he will go back to main menu
            mainMenu()
            menu_option = int(input('Your choice? '))
            if menu_option == 0:
                break


        elif playerChoice == 1 or playerChoice == 2:
            while True:
                position = input("Build where? ")          # from line 282- 295, it will basically ask where u want to place the building
                if position[0] == "a":
                    playerColumn = 1
                elif position[0] == "b":
                    playerColumn = 2
                elif position[0] == "c":
                    playerColumn = 3
                elif position[0] == "d":
                    playerColumn = 4
                if playerChoice == 1:
                    result = option1
                elif playerChoice == 2:
                    result = option2
                playerRow = int(position[1])

                for i in building:  # <---- this will subtract the amount of buildings when it is being chosen
                    if i[0] == str(option1):
                        i[1] -= 1

                    if i[0] == str(option2):
                        i[1] -= 1

                # this will check for illegal placement/ must build next to existing building
                if turn > 1:
                    if (board[playerRow + 1][playerColumn] == '   ' and board[playerRow - 1][playerColumn] == '   '
                            and board[playerRow][playerColumn + 1] == '   ' and board[playerRow][playerColumn - 1] == '   '):
                        print('You must build next to an existing building')




                    else:
                        if board[playerRow][playerColumn] == '   ':                      #this will check if its on an existing building,
                            board[playerRow][playerColumn] = str(result)                 #if it is, it will ask player to build on a different space.
                            turn += 1

                        else:
                            print('You cannot build on an existing building')


                        break
                else:
                    board[playerRow][playerColumn] = str(result)
                    turn += 1
                    break


        # this shows the remaining building
        elif playerChoice == 3:
            print('{:}{:>20}'.format('Building', 'Remaining'))
            print('{:}{:>20}'.format('--------', '---------'))
            for x, y in building:
                if y < 0:
                    y = 0
                print('{:}{:>20}'.format(x, y))

        # this shows current score
        elif playerChoice == 4:
            scoreBCH()
            scoreFAC()
            scoreHWY()
            scoreSHP()
            scoreHSE()

        # this saves the game
        elif playerChoice == 5:
            save_game(board, option1, option2, turn,building)

        # this checks if the input is not on the main menu e.g; 1,2,3,4,5,0 , it will give an invalid option and ask to repick option
        elif playerChoice != 1 or playerChoice != 2 or playerChoice != 3 or playerChoice != 4 or playerChoice != 5 or playerChoice != 0:
            print('Invalid option')


    if turn == 17:
        print('Final layout of Simp City: ')                #once the game is done, it will print the final layout, shows the score for each building
        printBoard()                                        #and shows the total score. it will also bring u back to the main menu
        scoreBCH()
        scoreFAC()
        scoreHSE()
        scoreSHP()
        scoreHWY()
        total = totalSHP + totalFAC + totalSHP + totalBCH + totalHWY
        print('Total score : ', total)
        mainMenu()
        menu_option = int(input("Your choice? "))





