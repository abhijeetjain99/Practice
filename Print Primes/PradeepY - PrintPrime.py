# Title: Program to print all the prime number less than or equal to a given
#        number. Input number should be an interger in range (1,10000].
# Author: Pradeep Yadav
# Date: 26/12/2017

def printPrime(limit):
    # Function to print all the prime numbers <= limit
    # Input: limit: integer, where limit > 1
    # Output: list of all prime numbers <= limit
    arrInit = [0] * (limit+1)
    arrInit[0] = -1
    arrInit[1] = -1
    index = 2
    num = 2
    count = 0
    while index < limit:
        if arrInit[index] == 0:
            print(index, end=" ")
            count += 1
            while index * num < limit: 
                arrInit[index * num] = -1
                num += 1
            num = 2
        index += 1
    print("\nToal prime numbers: {}".format(count))
    return

def main():
    maxLimit = int(input())
    printPrime(maxLimit)

if __name__=="__main__":
    main()
