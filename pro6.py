kn=int(input())
p1=list(map(int,input().split()))
v=0
for i in range(kn):
  for j in range(i,kn):
    for m in range(j,kn):
      if(p1[i]<p1[j]<p1[m]):
        v+=1
print(v)
