# -*- coding: utf-8 -*-
"""Find All Approximate combinations of a Pattern in a String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16SXFz9KNOFLTet9_dHkGYLYVbhNH14Nd
"""

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
            # print(i, end=" ")
            positions.append(text[i:i+len(pattern)])
    for i in positions:
        print(" ".join(positions))
        return positions


pattern = input()
text = input()
d = int(input())
ApproximatePattern(pattern, text, d)