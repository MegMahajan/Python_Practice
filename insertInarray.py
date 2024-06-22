import array as arr
# array(data_type,value_list)
a =arr.array('i',[1,2,3])
for i in range(0,3):
    print(a[i],end=" ")
print()
a.insert(1,4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()

b = arr.array('d',[2.5,3.2,55.2])
for i in range(0,3):
    print(b[i],end=" ")
print()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i,end=" ")
print()
