s1= int(input())
x=[]
for m in range(0,s1):
 chr=input()
 x.append(chr)
kn=[]
for m in zip(*x):
 if(m.count(m[0])==len(m)):
  kn.append(m[0])
 else:
  break
print(''.join(kn))
