#check if list is sorted

# if list is empty thn return True
# if list is having single value thm return True
# if list is curent elem is > next element then False

# def isSorted(l):
#     i = 1
#     while i < len(l):
#         if l[i] < l[i-1]:
#             return False
#         i += 1
#     return True
    
# def isSorted(l):
#    sl = sorted(l)
#    if sl == l:
#       return True
#    else:
#       return False

def isSorted(l):
    i = 1
    for i in range(i,len(l)):
        if l[i] < l[i-1]:
            return False
        i += 1
    return True


      
l =[100,20,3,40]

if isSorted(l):
    print("YES")
else:
    print("NO")      

           