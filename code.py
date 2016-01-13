import numpy as np

#Required Data
matrix_data =  [0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6]
toArray = np.array(matrix_data)
arrWinnerCheck =np.reshape(toArray, (-1,3))
#print arrWinnerCheck[7][2]


#Function To Check For The Winning Move    
def winOrNot(grid, ch):
    for i in xrange(8):
        if(grid[arrWinnerCheck[i][0]] == ch and grid[arrWinnerCheck[i][1]] == ch and grid[arrWinnerCheck[i][2]] == ch ):
            return True
    return False

#Function To Check For Validity of the grid
def validMovesOrNot(grid):
    xMovesCounter=0
    oMovesCounter=0
    #countMoves(grid)
    for i in xrange(9):
        if(grid[i]=='X'):
            xMovesCounter +=1
        if(grid[i]=='O'):
            oMovesCounter +=1
            
    if(xMovesCounter==oMovesCounter or xMovesCounter==oMovesCounter+1):
        if(winOrNot(grid, 'X') and xMovesCounter!=oMovesCounter+1):
              return False
        if(winOrNot(grid, 'O')):
           if(winOrNot(grid, 'X')):
              return False
           return (xMovesCounter==oMovesCounter)
        return True


##This is the main Code##

#user_input = raw_input()
inputFile = [line.rstrip('\n') for line in open('Q2.in')]
clearOutputFileContent = open('Q2.out','w').close()
#clearOutputFileContent.close()
inputTestCases = np.array(inputFile)
for i in xrange(len(inputTestCases)-1):
    programInput = inputTestCases[i]
    strToList = list(programInput)
    grid = np.array(strToList)
    #grid = np.reshape(A, (-1,3))
    outputFile=open('Q2.out','a')
    if(validMovesOrNot(grid)):
        print "valid"
        outputFile.write('valid\n') 
    else:
        print "invalid"
        outputFile.write('invalid\n') 
        
outputFile.close()              
#print B[1][1]
#print l[1]
