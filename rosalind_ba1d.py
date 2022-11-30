def pattern_matching(pattern, genome):
    for i in range(len(genome)-len(pattern)+1):
      if genome[i:i+len(pattern)] == pattern:
        print(i, end=" ")
    print()

pattern = input()
genome = input()
pattern_matching(pattern, genome)