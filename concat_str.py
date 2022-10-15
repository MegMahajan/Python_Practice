
def concat_int_num(n):
    result = ''
    for i in range(1, n + 1):
        result = result + str(i)
    return result


n = int(input("Enter the numbers for concat:\n"))
print(f"Final string is : ", concat_int_num(n))
