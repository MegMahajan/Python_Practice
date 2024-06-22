def removeDuplicates(arr,n):
    res = 1
    for i in range(1,n):
        if(arr[res-1]!= arr[i]):
            arr[res] = arr[i]
            res+=1

    return res

arr = [10,20,20,30,40,40]
n =6
print(removeDuplicates(arr,n))