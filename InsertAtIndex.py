# You are given an array arr(0-based index). The size of the array is given by sizeOfArray. You need to insert an element at given index.

# Input:
# sizeOfArray = 6
# arr[] = {1, 2, 3, 4, 5}
# index = 5, element = 90
# Output: 1 2 3 4 5 90
# Explanation: 90 is inserted at index
# 5(0-based indexing). After inserting,
# array elements are like
# # 1, 2, 3, 4, 5, 90.

class Solution:
    def insertAtIndex(self,arr,size,index,ele):
        arr.insert(index,ele)

    # You are given an array arr(0-based indexing). 
    # The size of the array is given by n. You need to update an element at the given index. 
    # The arr[i] of the array is initially set to i+1.

    # Input:
    # n = 5
    # index = 4,element = 8
    # Explanation: Element at 4th index updated to 8

    def updateArray(arr,n,idx,ele):
        arr[idx] = ele

    # Deletion means you need to shift all the elements after that index to the left by 1 position and set the last element as zero.

    # Input:
    # n = 5
    # index = 0
    # Output: 2 3 4 5 0

    def deleteFromArray(arr,n,idx):
        arr.pop(idx)
        arr.append(0)

        