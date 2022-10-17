def primeOrNot(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime num")
            break
    else:
        print(f"{num} is the prime num")


num = int(input("Enter the number for validation\n"))
if num > 1:
    primeOrNot(num)
else:
    print("Enter the valid number")
