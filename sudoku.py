import copy
import random
import time
def solver(puzzle, level = 0):
    #print level
    startPuzzle = copy.deepcopy(puzzle)
    range9 = range(9)
    if level == 0:
        for i in range9:
            for j in range9:
                if puzzle[i][j] == 0:
                    puzzle[i][j] = [1,2,3,4,5,6,7,8,9]
    # look through every cell and eliminate the choices that can be eliminated with the known cells 
    for row in range9:
        for column in range9:
            if type(puzzle[row][column]) == list: # if the cell is not already known
                if len(puzzle[row][column]) == 1: # if there is only one choice
                    puzzle[row][column] = puzzle[row][column][0] # make it known 
            if type(puzzle[row][column]) == int: # if it is known 
                for k in range9: 
                    if type(puzzle[row][k]) == list:
                        # clear the row
                        if puzzle[row][column] in puzzle[row][k]:
                            puzzle[row][k] = [item for item in puzzle[row][k] if item != puzzle[row][column]]
                            if puzzle[row][k] == []:
                                return False
                    if type(puzzle[k][column]) == list:
                        # clear the column
                        if puzzle[row][column] in puzzle[k][column]:
                            puzzle[k][column] = [item for item in puzzle[k][column] if item != puzzle[row][column]]
                            if puzzle[k][column] == []:
                                return False
                (square, rows, columns) = gridCell(row, column) # clear the square
                for i in rows:
                    for j in columns:
                        if type(puzzle[i][j]) == list:
                            puzzle[i][j] = [item for item in puzzle[i][j] if item != puzzle[row][column]]
                            if puzzle[i][j] == []:
                                return False
    # if two cells can only be two posibilities and are in a line clear the rest of the row of those cells
    #for row in range9:
        for a in range9:
            for b in range9:
                if a!=b and puzzle[row][a] == puzzle[row][b]:
                    if type(puzzle[row][a]) == list:
                        if len(puzzle[row][a]) == 2:
                            for c in range9:
                                if type(puzzle[row][c]) == list and c!=a and c!=b:
                                    puzzle[row][c] = [item for item in puzzle[row][c] if item not in puzzle[row][a]]
                                    if puzzle[row][c] == []:
                                        return False

                            
    # do the same as above but for columns 
    for column in range9:
        for a in range9:
            for b in range9:
                if a!=b and puzzle[a][column] == puzzle[b][column]:
                    if len(puzzle[a][column]) == 2:
                        for c in range9:
                            if type(puzzle[c][column]) == list and c!=a and c!=b:
                                puzzle[c][column] = [item for item in puzzle[c][column] if item not in puzzle[a][column]]
                                if puzzle[c][column] == []:
                                    return False
    # same as above but for squares  
    for square in range9:
        (rows, columns) = rowsColumnsForSquare(square)
        for a in rows:
            for b in rows:
                for c in columns:
                    for d in columns:
                        if (a,c)!= (b,d) and puzzle[a][c] == puzzle[b][d]:
                            if len(puzzle[a][c]) == 2:
                                for e in rows:
                                    for f in columns:
                                        if type(puzzle[e][f]) == list:
                                            if (e,f) != (a,c) and (e,f) != (b,d):
                                                puzzle[e][f] = [item for item in puzzle[e][f] if item not in puzzle[a][c]]
                                                if puzzle[e][f] == []:
                                                    return False
    if done(puzzle):
        return puzzle
    elif puzzle == startPuzzle:
        (guessPuzzle, elsePuzzle) = makeGuess(puzzle)
        donePuzzle = solver(guessPuzzle, level+1)
        if done(donePuzzle):
            return donePuzzle
        donePuzzle = solver(elsePuzzle, level+1)
        if done(donePuzzle):
            return donePuzzle
    else:
        donePuzzle = solver(puzzle, level+1)
        if done(donePuzzle):
            return donePuzzle

    
def makeGuess(puzzle):
    range9 = range(9) #[0,3,6,1,4,7,2,5,8]
    newPuzzle1 = copy.deepcopy(puzzle)
    newPuzzle2 = puzzle
    for i in range9:
        for j in range9:
            if type(puzzle[i][j]) == list:
                newPuzzle1[i][j] = puzzle[i][j][0]
                newPuzzle2[i][j] = puzzle[i][j][1:]
                return (newPuzzle1, newPuzzle2)
    

def done(puzzle):
    if type(puzzle) != list:
        return False
    for row in puzzle:
        for cell in row:
            if type(cell) == list or cell == 0:
                return False
    return True
def rowsColumnsForSquare(square):
    if square <3:
        rows = [0,1,2]
    elif square <6:
        rows = [3,4,5]
    else:
        rows = [6,7,8]
    if square %3 == 0:
        columns = [0,1,2]
    elif square %3 ==1:
        columns = [3,4,5]
    else:
        columns = [6,7,8]
    return (rows, columns)
def gridCell(row, column):
    a = [0,1,2]
    b = [3,4,5]
    c = [6,7,8]
    if row in a:
        rows = a
        if column in a:
            columns = a
            gridCell = 1
        elif column in b:
            columns = b
            gridCell = 2
        else:
            columns = c
            gridCell = 3
    elif row in b:
        rows = b
        if column in a:
            columns = a
            gridCell = 4
        elif column in b:
            columns =  b
            gridCell = 5
        else:
            columns = c
            gridCell = 6
    else:
        rows = c
        if column in a:
            columns = a
            gridCell = 7
        elif column in b:
            columns = b
            gridCell = 8
        else:
            columns = c
            gridCell = 9
    return (gridCell, rows, columns)
            



puzzleEasy = [[0,0,0,3,0,0,0,4,0],[0,0,2,1,0,4,6,5,9],[0,1,4,0,6,9,8,0,0],[0,0,0,8,0,7,3,0,0],[0,2,0,6,3,0,0,0,0],[0,3,0,0,2,0,0,0,5],[0,0,3,0,0,0,5,0,0],[1,0,0,2,9,0,0,3,8],[0,4,0,0,1,0,2,0,6]]
puzzleMiddle = [[9,0,5,2,0,0,8,4,3],[0,3,0,0,0,0,0,7,0],[4,0,0,6,0,8,0,0,0],[0,0,0,7,1,9,0,0,0],[0,0,0,8,5,0,0,0,0],[1,0,4,0,0,2,0,0,0],[0,0,6,9,4,3,2,8,0],[0,0,9,0,0,6,0,0,5],[0,1,0,0,8,0,0,0,0]]
puzzleHard = [[3,0,9,0,0,0,4,0,0],[4,8,0,0,0,0,0,0,0],[0,6,2,0,0,0,0,0,0],[2,3,0,0,5,4,7,0,0],[0,0,0,3,0,9,2,0,4],[0,0,0,8,0,0,3,5,1],[0,0,6,0,2,0,8,0,0],[0,0,0,0,9,0,0,0,0],[0,5,8,0,0,0,0,9,0]]
puzzleExpert = [[0,0,0,0,0,9,0,7,1],[0,0,4,0,3,0,0,0,0],[0,0,0,0,0,0,3,0,0],[3,0,0,0,0,0,0,8,0],[2,0,0,9,5,0,0,0,7],[0,0,0,7,0,1,0,0,3],[0,0,1,3,0,8,0,0,5],[9,0,0,1,0,0,0,0,0],[5,0,0,0,0,0,0,4,0]]
puzzleExtreme =[[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
puzzleExtreme2=[[0,6,1,0,0,7,0,0,3],[0,9,2,0,0,3,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,8,5,3,0,0,0,0],[0,0,0,0,0,0,5,0,4],[5,0,0,0,0,8,0,0,0],[0,4,0,0,0,0,0,0,1],[0,0,0,1,6,0,8,0,0],[6,0,0,0,0,0,0,0,0]]
empty = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
puzzles = [puzzleEasy, puzzleMiddle, puzzleHard, puzzleExpert, puzzleExtreme, puzzleExtreme2]
for puzzle in puzzles:
    for row in puzzle:
        print row
    startTime = time.time()
    donePuzzle = solver(puzzle)
    print "solved in " + str(time.time()-startTime) + " seconds"
    for row in donePuzzle:
        print row
    print "\n"
        


