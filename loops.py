#Print the elements of the following list using a loop:
# list = [1,4,9,16,25,36,49,64,81,100]

# for i in list:
#     print("the valu of list: ", i)

# #Search for a number x in this tuple using loop:
# tup = (1,4,9,16,25,36,49,64,81,100,49)
# x=49
# idx =0
# for i in tup:
#     if(i == x):
#         print("number found at idx: :", idx)
#         break
#     idx +=1

#Range example
# n=int(input("enter number..: "))
# for i in range(1,11):
#    print(i*n)


# for i in range(100, 0, -1):
#     pass

#WAP to find the sum of first n natural number(using while and for loop)
#Using for loop:

# n=6
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print("total sum of n numbers are: ", sum)

#using while loop

# n = int(input("Enter the number:"))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum of number:", sum)

#WAP to find the factorial of first n number (using for)

# !5 = !4 * 5
# !4 = !3 * 4
# !3 = !2 * 3

# n = int(input("Enter the number:"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print ("fact of n :", fact)

n = int(input("Enter the number:"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i +=1
print ("fact of n :", fact)