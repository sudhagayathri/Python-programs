# arr=[1,2,3,4,5,6]
# afterrot by 2
# res = [3,4,5,6,1,2]
arr = [1,2,3,4,5,6]
n = 6
d = int(input("enter place for rotation"))
temp =list()
for i in range(0,n):
    if(i+1<=d):
        temp.append(arr[i])
        print(i)
        arr.remove(arr[i])
print(arr)