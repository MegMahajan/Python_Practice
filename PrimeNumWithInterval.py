def primeOrNot(first, sec):
    for i in range(first, sec + 1):
        for j in range(2, i):
            if i % j == 0:
                #print(f"{i} is not a prime number")
                break
        else:
            print(f"{i} is a prime number")


firstinterval = int(input("Enter the first interval value\n"))
secinterval = int(input("Enter the sec interval value\n"))

if (firstinterval > 1 and secinterval > 2) and firstinterval < secinterval:
    primeOrNot(firstinterval, secinterval)
else:
    print("Enter the valid range")
