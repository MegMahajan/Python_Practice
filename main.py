print("Megha learning pyhton3!!! Keep learning.")
to_minutes = 24 * 60
to_units = 'minutes'


def calculate_mins(num_days):
    if num_days > 0:
        return f"{num_days} days are {num_days * to_minutes} {to_units}"
    else:
        return "You did not put correct number"


user_input = input("Hey User! Enter some number for number of days,which will convert into minutes\n")
number_of_days = int(user_input)
calculated_values = calculate_mins(number_of_days)
print(calculated_values)
