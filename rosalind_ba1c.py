string = input()
ans = " "
for i in string:
  if(i=="A"):
    ans+="T"
  elif(i=="C"):
    ans+="G"
  elif(i=="G"):
    ans+="C"
  elif(i=="T"):
    ans+="A"
print(ans[::-1])