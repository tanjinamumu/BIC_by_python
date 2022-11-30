
def frequent_words(text, k):
    di = {}
    kmers = []
    for i in range(len(text)-k):
        di[text[i:i+k]] = di.get(text[i:i+k],0)+1
    for i in di:
        if di[i] == max(di.values()): 
          kmers.append(i)
    return kmers

text = input()
k = int(input())
print(" ".join(frequent_words(text,k)))