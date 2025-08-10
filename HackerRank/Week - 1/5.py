def lonelyinteger(a):
    unique = 0
    for num in a:
        unique ^= num
    return unique

n = int(input().strip())
arr = list(map(int, input().split()))
print(lonelyinteger(arr))
