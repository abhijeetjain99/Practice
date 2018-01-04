# Title: This is a solution to the n-Queens problem using backtracking
# Author: Pradeep Yadav
# Date: 03/01/2018
# Problem Statement: The N Queen is the problem of placing N chess queens on
# an N×N chessboard so that no two queens attack each other.

def isValid(board, row, col):
    # Function to check if a certain position is valid, given a particular 
    # board configuration
    # Input: board: Current board configuration
    # row: row index to be checked
    # column: column index to be checked
    # Output: True, if current position does not have any conflict with other 
    # queens.
    
    for rowIndex in range(len(board)):
        for colIndex in range(len(board)):
            if abs(rowIndex-row) == abs(colIndex-col):   # Diagonal test
                if board[rowIndex][colIndex] == 1:
                    return False
            elif colIndex == col:                        # Column test
                if board[rowIndex][colIndex] == 1:
                    return False
            elif rowIndex == row:                        # Row test
                if board[rowIndex][colIndex] == 1:
                    return False
    return True
        
def PrintBoard(board):
    # Function to print a given board configuration
    # Input: board: A given board configuration( board will contain False when
    # the board does not have a solution)
    # Output: Print out board configuration
    
    if board == False:
        print("No Solution Exist")
    else:
        for row in board:
            print(row)

def PlaceQueen(board, row):
    # Function to place a queen in a given row
    # Input: board: Current board configuration
    # row: Row in which queen needs to be placed
    # Output: returns board configuration in case a solution exists otherwise 
    # return False 
    
    if row == len(board):                # If all the queens are alredy placed
        return True
    else:
        flag = False
        for col in range(len(board)):
            if isValid(board, row, col): # check if the board position is valid
                board[row][col] = 1
                flag = PlaceQueen(board, row + 1) # recursive call for next row
                if flag == False:           # if attempt to place queen failed
                    board[row][col] = 0     # try next column
                    continue
                else:
                    # If all the queens are successfully placed on the board 
                    # return board configuration
                    return board
                
        # Return false if unable to place queen
        return False                
            

def nQueens(noQueens):
    # Function to initialize the board and start the placement of queens
    # Input: noQueens: Number of queens
    # Output: Board configuration in case of success otherwise False
    
    board = [[0]*noQueens for _ in range(noQueens)]
    return PlaceQueen(board,0)
    
    
def main():
    noQueens = int(input("Enter Number of Queens: "))
    boardSolution = nQueens(noQueens)
    PrintBoard(boardSolution)                # Printing out board configuration

if __name__ == "__main__":
    main()
