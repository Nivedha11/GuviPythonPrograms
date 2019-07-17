k=int(input())
p1=3
q=3
m=1
for m in range(k-1):
    if(p1==1):
        p1=q*2
        q=p1
    else:
        p1=p1-1
print(p1)   
