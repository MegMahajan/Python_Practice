# def sum(a,b):
#     sum = a+b
#     return sum

# print(sum(2,3))

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     return avg

# print(calc_avg(1,2,3))

#WAF to print the length of any list

# cities =["Mumbai", "Pune", "Delhi", "Indore","khargone"]
# cars = ["Audi", "BMW", "Bens","Farrari"]

# def print_len(list):
#     print(len(list))
    
# print_len(cities)
# print_len(cars)

# WAF to print the elements of a list in a single line(List of parameter)

# def print_list(list):
#     for item in list:
#        print(item, end=" ")

# print_list(cities)
# print()



# WAF to find the factorial of n (n is the parameter)
# Fact !3=1*2*3

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(3)

# wAF to convert USD to INR

#1 usd = 83 Rup

def convertUSD(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

convertUSD(100)