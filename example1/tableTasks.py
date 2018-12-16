import random
S=0
M=0
Max=0
Min=0
l = range(10)
for i in range(10):
      l[i]= random.randrange(0, 101)
      S=S+l[i]

M=S/10
Max, Min = l[0], l[0]  
for i in range(len(l) - 1):
    
    if Max<l[i+1]:
        Max=l[i+1]
    
    if Min>l[i+1]:
        Min=l[i+1]

print ('table',l)
print ('Somme',S)
print ('Moyenne',M)
print('minimum',Min)
print('maximum',Max)

Table = [1,5,10,15,20,25,30,25,20,7,3]
Doublon = Table[0]

numbers = len(Table)
for i in range(1, numbers):
  for j in range(i, numbers):
    if Table[j] == Doublon:
      Table[j] = 'X'
  Doublon = Table[i]
    
palindrom = (lolol)
for i in (len(plindrom)-1)
    if palindrom[0]=palindrom[(len(palindrom)-1)]
    print (c"'"est un palindrom)
    else:
        print (ce n"'"est pas un palindrom)

espace = "e s p a c e"
espace = espace.replace(" ","")
print espace


isPalindrom = True
palindrom = ("")
if len(palindrom)>0:
    for i in range(len(palindrom)/2+1):
        if palindrom[i] != palindrom[(len(palindrom)-i-1)]:
            isPalindrom = False
            break
print isPalindrom