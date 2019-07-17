kn=list(input())
m1=len(kn)
new=''
for v in range (0,m1,2):
    kn[v],kn[v+1]=kn[v+1],kn[v]
print(*kn,sep='')
