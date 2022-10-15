a = "Shaarvil"
print(len(a))


# Without in built method
def lenth_of_string(name):
    len_count = 0
    for i in name:
        len_count = len_count + 1
    return len_count


name = input("Enter any words for checking length\n")
my_string = lenth_of_string(name)
print(f"Length of given string is {my_string}")
