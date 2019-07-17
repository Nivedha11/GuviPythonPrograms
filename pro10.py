k1=int(input())
m1=list(map(int,input().split()))
n1=0
for p in range(0,k1):
  for q in range(0,p):
    if(m1[q]<m1[p]):
      n1=n1+m1[q]
print(n1)
