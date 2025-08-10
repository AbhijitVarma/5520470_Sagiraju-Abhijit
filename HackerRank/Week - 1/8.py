def countingSort(arr):
    freq = [0] * 100
    for num in arr:
        freq[num] += 1
    return freq

n = int(input().strip())
arr = list(map(int, input().split()))
print(*countingSort(arr))
