kn=list(map(int,input().split()))
mn=list(map(int,input().split()))
for l in range(0,kn[1]):
  mn=[mn[-1]] + mn[:-1]
print(*mn,end=' ')
