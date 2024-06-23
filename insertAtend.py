# You are given an array arr. The size of the array is given by sizeOfArray. You need to insert an element at the end.
# Array already have the sizeofarray -1 elements.

# Input:
# sizeOfArray = 6
# arr[] = {1, 2, 3, 4, 5}
# element = 90
# Output: 1 2 3 4 5 90
# Explanation: After inserting 90 at the
# end, we have array elements as 
# 1 2 3 4 5 90.

def insertAtEnd(arr,N,ele):
    arr.appenf(ele)

