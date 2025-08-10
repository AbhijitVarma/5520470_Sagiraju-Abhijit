def birthday(s, d, m):
    count = 0
    n = len(s)
    
    # Loop through each starting index
    for i in range(n - m + 1):
        # Check if the sum of this segment matches Ron's birth day
        if sum(s[i:i+m]) == d:
            count += 1
            
    return count

# Reading input
n = int(input().strip())
s = list(map(int, input().split()))
d, m = map(int, input().split())

print(birthday(s, d, m))
