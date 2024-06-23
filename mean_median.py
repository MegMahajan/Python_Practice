# Given an array a[ ] of size N. The task is to find the median and mean of the array elements. Mean is average of the numbers and median is the element which is smaller than half of the elements and greater than remaining half.  If there are odd elements, the median is simply the middle element in the sorted array. If there are even elements, then the median is floor of average of two middle numbers in the sorted array. If mean is floating point number, then we need to print floor of it.

# Note: To find the median, you might need to sort the array. Since sorting is covered in later tracks, we have already provided the sort function to you in the code.

# Input:
# N = 5
# a[] = {1, 2, 19, 28, 5}
# Output: 11 5
# Explanation: For array of 5 elements,
# mean is (1 + 2 + 19  + 28  + 5)/5 = 11.
# Median is 5 (middle element after 
# sorting)


import math


class Solution:
    def median(self,A,N):
        A = list(A)
        A.sort()

        if N % 2 == 1:
            median = A[N // 2]
        else:
            median = (A[N //2 - 1] + A[N // 2]) // 2

        return median
    
    def mean(self, A, N):
        sum = 0
        N = len(A)
        for i in A:
            sum += i
        mean = sum/N

        return math.floor(mean)
    
