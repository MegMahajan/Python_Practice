class Solution:
    def majorityOcc(self, arr,n,x,y):
             
         count_x = 0
         count_y = 0

         for i in arr:
              if i == x:
                   count_x +=1
              elif i == y:
                   count_y +=1

         if count_x > count_y:
              return x
         elif count_y > count_x:
              return y
         else:
              return min(x,y)



sol = Solution()
s = sol.majorityOcc([98, 99 ,39 ,12 ,0 ,36 ,15, 47, 79, 62, 64],11,64,5)
print(s)

           