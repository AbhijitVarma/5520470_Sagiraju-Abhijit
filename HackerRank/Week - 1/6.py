def flippingBits(n):
    return n ^ 0xFFFFFFFF

q = int(input().strip())
for _ in range(q):
    num = int(input().strip())
    print(flippingBits(num))
