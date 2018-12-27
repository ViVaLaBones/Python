arr1: str = open("text.txt").read()

arr2: str ="Lösung:"
for x in arr1:
    if ord(x)>96 and ord(x)<123:
        arr2 = arr2 + x



print(arr2)