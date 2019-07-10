kn,sm=input().split()
d1=abs(len(kn)-len(sm))
for j in range(len(kn)):
  if len(sm)==1 and sm[j] in kn:
    break
  if kn[j]!=sm[j]:
    d1=d1+1
print(d1)
