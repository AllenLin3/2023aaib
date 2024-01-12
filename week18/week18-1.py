N=len(s)
a=s[:N//2]
b=a[N//2:]
motherA=0
motherB=0
for c in a:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        motherA +=1
    if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
        motherB+=1
for c in a:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        motherA +=1
    if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
        motherB+=1
if motherA == motherB: return True
else:return False
============
N=len(s)
a=s[:N//2]
b=a[N//2:]
motherA=0
motherB=0
mother='aeiouAEIOU'
for c in a:
   if c in mother:motherA+=1
for c in b:
    if c in mother:motherB+=1
if motherA == motherB: return True
else:return False


