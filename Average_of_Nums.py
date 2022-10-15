def collection_of_nums(totalnumber):
    print(f"Please enter all the numbers , {totalnumber}")
    for i in range(0, totalnumber):
        ele = float(input())
        myList.append(ele)


def calculate_average():
    total = 0
    for i in range(0, len(myList)):
        total = total + myList[i]
    return total / total_numbers


myList = []
total_numbers = int(input("Enter the Average of how many number you want?"))
collection_of_nums(total_numbers)

average = calculate_average()
print(f"The average of all the {average} numbers")
