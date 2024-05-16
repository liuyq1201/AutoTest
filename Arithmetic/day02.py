import json
def serch(arr, tar: int):
    l = 0
    r = len(arr)
    n = 0
    while (l <= r - 1):
        mid = (l + r) // 2
        if tar == arr[mid]:
            return mid
        if tar > arr[mid]:
            l = mid - 1
        else:
            r = mid + 1
        n = n + 1
        print(n)
    return -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(serch(a, 7))



n=None
m="a"
print(str(n)+m)
s='12345677890'
print(s[0:5])

