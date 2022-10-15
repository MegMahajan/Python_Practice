def posNegZeroValidate(input_number):
    if (input_number == 0):
        print("The number is zero")
    elif (input_number > 0):
        print("The number is positve number")
    else:
        print("The number is negative number")


input_number = float(input("Enter any number:\n"))
posNegZeroValidate(input_number)
