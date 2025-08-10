def twoArrays(k, A, B):
    # Sort A in ascending order and B in descending order
    A.sort()
    B.sort(reverse=True)
    
    # Check if each pair meets the condition A[i] + B[i] >= k
    for a, b in zip(A, B):
        if a + b < k:
            return "NO"
    return "YES"

# Reading input
q = int(input().strip())
for _ in range(q):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(twoArrays(k, A, B))
