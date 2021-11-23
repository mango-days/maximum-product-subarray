# Given an integer array, find the subarray that has the maximum product of its elements. The solution should return the maximum product of elements among all possible subarrays.
# Input:  { 40, 0, -20, -10 }
# Output: 200
# Explanation: The maximum product subarray is {-20, -10} having product 200
array = [ -6, 4, -5, 8, -10, 0, 8 ]
max_product = -1
sub_array = []
n = len ( array ) - 2
while n != 0 : 
    for index in range ( 0 , len ( array ) - n + 1 ) :
        temp = 1
        for index2 in range ( index , index + n ) : temp *= array [ index2 ]
        if temp > max_product : 
            max_product = temp
            sub_array = array [ index : index + n ]
    n -= 1
print ( max_product , sub_array)