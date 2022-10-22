def clump_finding(s, k, L, t):
    res = []
    for i in range(len(s)-L+1):
        for j in range(i,i+L-k):
            if s[i:i+L].count(s[j:j+k]) == t:
                res.append(s[j:j+k])
    res = list(set(res))
    return res
    
s = input()
k= int(input())
L= int(input()) 
t = int(input())

res = clump_finding(s, k, L, t)
print(" ".join(res))