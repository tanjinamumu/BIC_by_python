def frequent_words(text, k): #function 
    frequent_pattern = {} #empty string
    length = len(text) #length of text
    for i in range(length-k+1): #for loop upto text-K+1
        if text[i:i+k] not in frequent_pattern: 
            frequent_pattern[text[i:i+k]] = 0 
        frequent_pattern[text[i:i+k]] += 1 
    frequent_count = max(frequent_pattern.values()) 
    for k,v in frequent_pattern.items(): 
        if v==frequent_count: 
            print(k, end=" ") #prints k-mer
    print()
    return frequent_pattern
    
text = input()
k = int(input())
frequent_words(text, k)