import urllib.request


arr1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

arr2 = urllib.request.urlopen(arr1)

print(arr2)