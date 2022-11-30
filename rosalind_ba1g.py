string1 = input();
string2 = input();
S1 = len(string1);
S1 = len(string2);
ans = 0;

for i in range(0, S1):
    if (string1[i] != string2[i]):
       ans+=1;
print(ans)