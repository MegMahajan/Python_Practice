
index = int(input("Enter the index value till u want the series:\n"))
firstno=0
secno=1
temp=0
#print(firstno)
#print(secno)
for i in range(0,index):
    temp = firstno + secno
    firstno = secno
    secno =temp
    print(temp)
