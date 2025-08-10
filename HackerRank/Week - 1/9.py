def pangrams(s):
    letters = set(s.lower())
    return "pangram" if all(chr(c) in letters for c in range(ord('a'), ord('z') + 1)) else "not pangram"

s = input()
print(pangrams(s))
