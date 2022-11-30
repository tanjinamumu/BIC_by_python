sequence = input()

def skew(sequence):
    c = 0
    g = 0
    min_skew = 0
    skew_list = []
    index = 0
    for i in sequence:
        index += 1
        if i == 'C':
            c += 1
        if i == 'G':
            g += 1
        skew = g-c
#         print(skew)
        if skew < min_skew:
            skew_list = [index]
#             print(skew_list)
            min_skew = skew
#             print(min_skew)
        if skew == min_skew and index not in skew_list:
            skew_list.append(index)
    print(skew_list)
skew(sequence)



