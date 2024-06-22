#Reveres a given list 

def reverselist(l):
    s = 0
    e = len(l) - 1

    while s < e:
        l[s],l[e] = l[e], l[s]
        s = s+1
        e = e-1





l = ["1","2","23", "asdf"]
reverselist(l)
#l.reverse()
#new_l=l[::-1]
print(l)