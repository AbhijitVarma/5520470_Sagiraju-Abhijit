def matchingStrings(strings, queries):
    counts = []
    for q in queries:
        counts.append(strings.count(q))
    return counts

n = int(input().strip())
strings = [input().strip() for _ in range(n)]
q = int(input().strip())
queries = [input().strip() for _ in range(q)]

result = matchingStrings(strings, queries)
for r in result:
    print(r)
