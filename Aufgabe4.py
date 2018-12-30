import urllib.request



arr1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
arr11: str = "8022"            #12345 #16044/2
arr3: str



while 1:
    url = arr1 + arr11
    arr2 = urllib.request.urlopen(url).read()
    print(arr2)

    arr3 = arr2[len(arr2)-10:]
    arr3 = arr3.decode()
    arr11 = ""
    #print(arr3)
    for x in arr3:
        if ord(x) > 47 and ord(x) < 58:
            arr11 = arr11 + x
    arr4 = int(arr11)
    arr4 = round(arr4)
    #print(arr4)
    arr11 = str(arr4)
    #print(arr11)
