# Given an array arr[] of size N containing positive integers and an integer X. You need to find the value in the array which is greater than X and closest to it. ( if no such value exists the answer should be -1)

# Example 1:

# Input:
# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Output: 67
# Explanation: For a given value 16, there
# is only one value 67 that greater than
# it and so it is the answer.

class Solution:
   
    def immediateGreater(self,arr,n,x):
        closest = -1
        for i in arr:
            if(i > x):
                if ( closest == -1 or i < closest ):
                    closest = i
                
            
        return closest 
               
                
sol = Solution()
s = sol.immediateGreater([63, 6, 60, 38, 3, 94, 43, 83, 65],9,18)
print(s)
