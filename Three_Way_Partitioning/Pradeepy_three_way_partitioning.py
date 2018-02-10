# Title: Partitioning a list in three ways according to given range
# Author: Pradeep Kumar Yadav
# Date: 10/02/2018

import numpy as np                 # for generating random numbers
#np.random.seed(0)                 # for generating same values for testing purpose
    
def Swap(num_list, index1, index2):
    # Funtion to swap elements of the array
    # Input: num_list: Given Array
    # index1, index2: Positions needs to be swapped 
    
    num_list[index2], num_list[index1] = num_list[index1], num_list[index2]
    return num_list

def ThreeWaySort(num_list, _range):
    # Fcuntion to perform three way partitioning
    # Input: num_list: List to be partitioned
    # _range: Range values in the form of a list
    
    index = 0
    start = 0
    end = len(num_list) - 1  
    while index <= end:
        if num_list[index] < _range[0] and index >= start:
            num_list = Swap(num_list, index, start)
            start = start + 1
            continue
        
        if num_list[index] > _range[1] and index <= end:
            if num_list[end] > _range[1]:
                end = end - 1
                continue
            else:
                num_list = Swap(num_list, index, end)
                end = end - 1
                continue
            
        index = index + 1
    return num_list
        
def main():
    num_list = list(np.random.randint(1,100,(15,)))
    print("Num List: ",num_list)
    _range = [35,60]
    print("Range: ",_range)
    num_list = ThreeWaySort(num_list, _range)
    print("After Partitioning: ",num_list)

if __name__ == "__main__":
    main()
