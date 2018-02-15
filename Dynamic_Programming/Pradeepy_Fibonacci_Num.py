# Title: Program to calculate a fibonacci number from the fibonacci series using
# dynamic programming(Memoization).
# Author: Pradeep Kumar Yadav
# Date: 13/02/18

fibDict = {0:0, 1:1}  # Dictionary to store calculated intermediate results

def Fibonacci(num):
    # Function to calculate a particular fibonacci number
    # Input: num: index of the number in series
    # Output: fibonacci number at given index
    
    if num in fibDict.keys():
        return fibDict[num]
    else:
        fibVal = Fibonacci(num-1) + Fibonacci(num-2)
        fibDict[num] = fibVal
        return fibVal

def main():
    num = int(input("Enter the Position: "))
    fibNum = Fibonacci(num)
    print(fibNum)

if __name__ == "__main__":
    main()
