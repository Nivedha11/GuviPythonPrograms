num=int(input())
p=list(map(int,input().split()))
kn=[]
for l in range(num):
    if p[l]==l:
        kn.append(str(p[l]))
        kn.sort()
if len(kn)==0:
    print("-1")
else:
    print(" ".join(kn))
