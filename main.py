arr = [1,2,2,3,1]
newarr =[]
for i in range(0,len(arr)):
    if arr[i] not in newarr:
        newarr.append(arr[i])
for i in range(0,len(newarr)):
    print(newarr[i] ,"->",arr.count(newarr[i]))