s= input()
code=[]
patternl = 0
letter= int(input())+1
y=1
for x in range(len(s)):
    if s[x].isalpha():
      code.append(s[x])
for x in range(len(s)):
    if s[x].isalpha():
       s = s.replace(s[x], " ") 
numA= s.split()
for y in range(len(numA)):
  patternl = patternl + int(numA[y])
remainder= letter%patternl
if remainder==0:
   let= code[-1]

else:
    for z in range(len(numA)):
        remainder = remainder- int(numA[z])
        if remainder <=0:
            let= code[z]
            break
print(let)
   

