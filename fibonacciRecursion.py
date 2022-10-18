def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibo(i - 2) + fibo(i - 1)


index = int(input("Enter the index value till u want the series:\n"))

if index <= 0:
    print("Provide positive number")
else:
    for i in range(0, index):
        print(fibo(i))
