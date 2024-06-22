#get a list as input from user in python

#lst =[]
# n = int(input("Enter number of elements: "))

# for i in range(0,n):
#     ele = int(input("enter the numbers you mentions: 3"))
#     lst.append(ele)
# print(lst)

#Get a List as input from user in python with exception handling

try:
    lst = []
    while True:
        lst.append(int(input("keep entering numbers")))
    

except:
    print(lst)
