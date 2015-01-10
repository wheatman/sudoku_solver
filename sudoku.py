import copy
import random
def solver(puzzle, level = 0, guess = 0):
    startPuzzle = copy.deepcopy(puzzle)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                puzzle[i][j] = [1,2,3,4,5,6,7,8,9]
    a = [0,1,2]
    b = [3,4,5]
    c = [6,7,8]
    for row in range(9):
        for column in range(9):
            if type(puzzle[row][column]) != int:
                if len(puzzle[row][column]) == 1:
                    puzzle[row][column] = puzzle[row][column][0]
            if type(puzzle[row][column]) == int:
                for k in range(9): # clear the row
                    if type(puzzle[row][k]) != int:
                        puzzle[row][k] = [item for item in puzzle[row][k] if item != puzzle[row][column]]
                for k in range(9): # clear the comumn
                    if type(puzzle[k][column]) != int:
                        if puzzle[row][column] in puzzle[k][column]:
                            puzzle[k][column] = [item for item in puzzle[k][column] if item != puzzle[row][column]]
                (square, rows, columns) = gridCell(row, column) # clear the square
                for i in rows:
                    for j in columns:
                        if type(puzzle[i][j]) != int:
                            puzzle[i][j] = [item for item in puzzle[i][j] if item != puzzle[row][column]]
    for row in range(9):
        for a in range(9):
            for b in range(9):
                if a!=b and type(puzzle[row][a]) == list and type(puzzle[row][b]) == list:
                    if len(puzzle[row][a]) == 2 and len(puzzle[row][b]) == 2 and puzzle[row][a] == puzzle[row][b]:
                        for c in range(9):
                            if type(puzzle[row][c]) == list and c!=a and c!=b:
                                puzzle[row][c] = [item for item in puzzle[row][c] if item not in puzzle[row][a]]
    for column in range(9):
        for a in range(9):
            for b in range(9):
                if a!=b and type(puzzle[a][column]) == list and type(puzzle[b][column]) == list:
                    if len(puzzle[a][column]) == 2 and len(puzzle[b][column]) == 2 and puzzle[a][column] == puzzle[b][column]:
                        for c in range(9):
                            if type(puzzle[c][column]) == list and c!=a and c!=b:
                                puzzle[c][column] = [item for item in puzzle[c][column] if item not in puzzle[a][column]]
    for square in range(1,10):
        (rows, columns) = rowsColumnsForSquare(square)
        for a in rows:
            for b in rows:
                for c in columns:
                    for d in columns:
                        if (a,c)!= (b,d) and puzzle[a][c] == puzzle[b][d]:
                            if type(puzzle[a][c]) == list and type(puzzle[b][d]) == list:
                                if len(puzzle[a][c]) == 2 and len(puzzle[b][d]) == 2:
                                    for e in rows:
                                        for f in columns:
                                            if type(puzzle[e][f]) == list:
                                                if (e,f) != (a,c) and (e,f) != (b,d):
                                                    puzzle[e][f] = [item for item in puzzle[e][f] if item not in puzzle[a][c]]
    for row in puzzle:
        for cell in row:
            if cell == []:
                return False
    if puzzle == startPuzzle:
        guessPuzzle = copy.deepcopy(puzzle)
        if makeGuess(guessPuzzle):
            print "start guess"
            solver(guessPuzzle, level+1)
    else:
        solver(puzzle, level+1)
def makeGuess(puzzle):
    options = []
    for i in range(9):
        for j in range(9):
            if type(puzzle[i][j]) == list:
                if len(puzzle[i][j])!= 0:
                    options.append([i,j,len(puzzle[i][j])])
                else:
                    return False
    minpos = 9
    for item in options:
        if item[2]<minpos:
            minpos = item[2]
    for item in options:
        if item[2]>minpos:
            options.remove(item)
    print 1
    print options
    print 1
    if len(options)==0:
        return False
    elif len(options)==1:
        rand = 0
    else:
        rand = random.randint(0,len(options)-1)
    puzzle[options[rand][0]][options[rand][1]] = puzzle[options[rand][0]][options[rand][1]][0]
    return True
    
                


def done(puzzle):
    for row in puzzle:
        for cell in row:
            if type(cell) == list or cell == 0:
                return False
    return True
def rowsColumnsForSquare(square):
    a = [0,1,2]
    b = [3,4,5]
    c = [6,7,8]
    if square in [1,2,3]:
        rows = a
    if square in [4,5,6]:
        rows = b
    if square in [7,8,9]:
        rows = c
    if square in [1,4,7]:
        columns = a
    if square in [2,5,8]:
        columns = b
    if square in [3,6,9]:
        columns = c
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
        if column in b:
            columns = b
            gridCell = 2
        if column in c:
            columns = c
            gridCell = 3
    if row in b:
        rows = b
        if column in a:
            columns = a
            gridCell = 4
        if column in b:
            columns =  b
            gridCell = 5
        if column in c:
            columns = c
            gridCell = 6
    if row in c:
        rows = c
        if column in a:
            columns = a
            gridCell = 7
        if column in b:
            columns = b
            gridCell = 8
        if column in c:
            columns = c
            gridCell = 9
    return (gridCell, rows, columns)
            



puzzleEasy = [[0,0,0,3,0,0,0,4,0],[0,0,2,1,0,4,6,5,9],[0,1,4,0,6,9,8,0,0],[0,0,0,8,0,7,3,0,0],[0,2,0,6,3,0,0,0,0],[0,3,0,0,2,0,0,0,5],[0,0,3,0,0,0,5,0,0],[1,0,0,2,9,0,0,3,8],[0,4,0,0,1,0,2,0,6]]
puzzlenext = [[9,0,5,2,0,0,8,4,3],[0,3,0,0,0,0,0,7,0],[4,0,0,6,0,8,0,0,0],[0,0,0,7,1,9,0,0,0],[0,0,0,8,5,0,0,0,0],[1,0,4,0,0,2,0,0,0],[0,0,6,9,4,3,2,8,0],[0,0,9,0,0,6,0,0,5],[0,1,0,0,8,0,0,0,0]]
puzzle = [[3,0,9,0,0,0,4,0,0],[4,8,0,0,0,0,0,0,0],[0,6,2,0,0,0,0,0,0],[2,3,0,0,5,4,7,0,0],[0,0,0,3,0,9,2,0,4],[0,0,0,8,0,0,3,5,1],[0,0,6,0,2,0,8,0,0],[0,0,0,0,9,0,0,0,0],[0,5,8,0,0,0,0,9,0]]
for row in puzzle:
    print row
print "start"
while not done(puzzle):
    solver(puzzle)
    for row in puzzle:
        print row
for row in puzzle:
    print row

