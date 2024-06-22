#Avg of a list

# def avg(l):
#     return sum(l)/len(l)

# l= [1,2,3,4,5]
# print(avg(l))


#Seperate Even & ODD

 #l =[10,41,30,15,80]
 #evenList =[]
 #oddList =[]
# def seperate(l):
#     for i in l:
#         if(i % 2 == 0):
#             evenList.append(i)
#         else:
#             oddList.append(i)
#     return evenList,oddList

def seperate(l):
    evenList= [e for e in l if e % 2 == 0 ]
    oddList = [x for x in l if x % 2 != 0 ]
    return evenList,oddList
l =[10,41,30,15,80]
e,o=seperate(l)
print(e)
print(o)

#get smaller elements
# newlist = []
# def getsmaller(l,x):
#     for i in l:
#         if(i < x):
#             newlist.append(i)
#     return newlist

# def getsmaller(l,x):
#     return [e for e in l if e < x]

# l= [8,100,20,40,3,7]
# x=10
# print(getsmaller(l,x))