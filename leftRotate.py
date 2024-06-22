l = [10,20,30,40]
# l = l[1:] + l[0:1]
#l.append(l.pop(0))

def rotateByOne(l):
    n =len(l)
    x =l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x
rotateByOne(l)
print(l)

