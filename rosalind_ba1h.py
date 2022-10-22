def HammingDistance(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d

def ApproximatePattern(pattern, text, d):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            print(i, end=" ")
            positions.append(i)
    return positions


pattern = input()
text = input()
d = int(input())
ApproximatePattern(pattern, text, d)