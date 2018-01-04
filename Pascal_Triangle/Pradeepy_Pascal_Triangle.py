# Title: Program to print first n rows of a Pascal's triangle.
# Author: Pradeep Yadav
# Date: 05/01/2018

def PascalTriangle(noRows):
    # Function to generate Pascal traingle
    # Input: Number of rows
    # Output: Pascal triangle as 2D array
    
    arr = [[1]*noRows for _ in range(noRows)]
    for row in list(range(1,noRows)):
        for col in list(range(1,noRows- row)):
            arr[row][col] = arr[row][col-1] + arr[row-1][col]  
    return arr

def PrintPascal(arr):
    # Function to print Pascals triangle 
    # Input: 2D array 
    # Output: Print pascal triangle
    
    midIndex = len(arr)//2             # Index of the biggest term in triangle
    if len(arr)%2 == 0:
        maxDigit = len(str(arr[midIndex][midIndex-1]))         # no. of digits
    else:
        maxDigit = len(str(arr[midIndex][midIndex]))
    
    # Printing triangle with even space between elements
    for row in range(len(arr)):
        print("{:^}".format(' '*maxDigit*(len(arr)-row)),end='')
        for col in range(row+1):
            print("{1:^{0:}}".format(maxDigit, arr[row-col][col]),end="")
            print(" "*maxDigit,end='')
        print("{:^}".format(' '*maxDigit*(len(arr)-row)))

def main():
    noRows = int(input("Enter Rows: "))
    pascalTriangle = PascalTriangle(noRows)
    PrintPascal(pascalTriangle)

if __name__ == "__main__":
    main()
