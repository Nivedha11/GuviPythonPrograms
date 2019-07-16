kn1,sm1=list(map(int,input().split()))
lis=list(map(int,input().split()))
for v in range(sm1):
  p,q=list(map(int,input().split()))
  print(sum(lis[p-1:q]))
