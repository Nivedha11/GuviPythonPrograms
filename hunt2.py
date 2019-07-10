kn=int(input())
kn=list(map(int,input().split()))
kn.sort()
kn.reverse()
if kn[0]==0:
    print("0")
else:
    for l in kn:
        print(l,end='')
