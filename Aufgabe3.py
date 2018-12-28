arr1 = open("Aufgabe3.txt").read()
arr2 = "Die Lösung:"
i:int = -1

for x in arr1:
    i = i + 1
    if x.islower():
        if arr1[i-4].islower() and arr1[i-1].isupper() and arr1[i-2].isupper() and arr1[i-3].isupper() and arr1[i+1].isupper() and arr1[i+2].isupper() and arr1[i+3].isupper() and arr1[i+4].islower():
            arr2 = arr2 + x





print(arr2)