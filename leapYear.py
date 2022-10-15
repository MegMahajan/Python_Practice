def is_leap_year(year):
    if ((year % 400 == 0) | (year % 100 != 0)) & (year % 4 == 0):
        return True
    else:
        return False


year = int(input("enter any year to find that year is leap year or not : \n"))
print(is_leap_year(year))
