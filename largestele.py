# def getmax(l):
#     for x in l: #10,20,3
#         print("x in for loop: ", x )
#         for y in l: #10,20,3,50
#             print("y in for loop: ", y )
#             if y > x: # 20,50,50
#                 break 
#         else:
#             return x
        
#     return None

def getMax(l):
    if not l:
        return None
    else:
        res =l[0]
        for i in range(1,len(l)):
            print("i in for loop: ", i )
            if l[i] > res:
                print("l[i] in for loop: ", l[i] )
                res = l[i]
                print("res inside for loop: ", res )
        return res

l= [10,244,344, 50]
print(getMax(l))