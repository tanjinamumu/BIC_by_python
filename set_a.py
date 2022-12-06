# -*- coding: utf-8 -*-
"""Set-A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mk6UyMEI0RHfj1d1MS7qbkNojizq_AMp
"""

def frequent_words(text, k, t): #function 
    frequent_pattern = {} #empty string
    count=0
    temp=0
    ans = " "
    for i in range(len(text)-k+1): #for loop upto text-K+1
        if text[i:i+k] not in frequent_pattern: 
            frequent_pattern[text[i:i+k]] = 0 
        frequent_pattern[text[i:i+k]] += 1 
    frequent_count = max(frequent_pattern.values()) 
    for k,v in frequent_pattern.items(): 
        if v==frequent_count and v==t: 
            # print(k[::-1])
            count+=1
            ans+=k
    if count==1:
            print(ans[::-1])
             
    else:
      print("Alas! I lost the game.")

text = input()
k = int(input())
t = int(input())
frequent_words(text, k, t)