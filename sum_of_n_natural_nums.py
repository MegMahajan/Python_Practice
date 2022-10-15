def sum_of_n_num(n_numbers):
    return (n_numbers * (n_numbers + 1)) / 2


n_numbers = float(input("Enter the natural numbers:\n"))
if n_numbers > 0:
    print(f"The sum of n natural numbers is: ",sum_of_n_num(n_numbers))
else:
    print("Please enter valid number")
