kn1=list(map(str,input()))
set1=s1=0
for v in range(0,len(kn1)-1):
  p=kn1[v]
  if int(p)!=0:
   for j in range(v+1,v+2):
    p=p+kn1[j]
    if int(p)<27 and int(p)>0: set1=set1+1
    elif int(p)==0: set1=set1-1
    else: break
if set1!=1: s1=set1%2
print(set1+s1+1)
