# Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it

# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Output: 15
# Explanation: For a given value 16, there
# are four values which are smaller than
# it. But 15 is the number which is smaller
# and closest to it with minimum difference
# of 1.

class Solution:
    def immediateSmallerThanX(self,arr,n,x):

        closest = None
        min_diff = float('inf')

        for i in arr:
            if i < x:
                diff = x - i 
                if diff < min_diff:
                    closest = i
                    min_diff = diff

            if closest is None:
                return -1
            
            return closest