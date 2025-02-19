s= "tgt"
code=[]
for x in range(len(s)):
    if s[x].isalpha():
      code.append(s[x])
      s = s.replace(s[x], " ") 
print(code)