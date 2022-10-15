def input_two_numbers():
    try:
        a = int(input("Enter the value of a:"))
        b = int(input("Enter the value of b:"))
        print(f"Initially the value of a is {a} and the value of b is {b}")
        temp: int = a
        a = b
        b = temp

        print(f"Now value of a is {a} and the value of b is {b}")
    except:
        print("Provide digits only")

input_two_numbers()

#Swapping without temp or third variables:
def swapping_without_temp():
    try:
        a = int(input("Enter the value of a:"))
        b = int(input("Enter the value of b:"))
        print(f"Initially the value of a is {a} and the value of b is {b}")
        a = a + b
        b = a - b
        a = a - b
    except:
        print("Provide digits only")


