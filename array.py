import array
arr = array.array('i',[])
for i in range(0,5):
    x = int(input("enter the values in the array"))
    arr.append(x)
print(arr)