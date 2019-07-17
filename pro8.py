import math
k1,n1=map(int,input().split())
m=[]
v=list(map(int,input().split()))
for i in range(0,n1):
        p1,q1 =map(int,input().split())
        m.append([p1,q1])
for i in m:
        x1=i[0]-1
        y1=i[1]-1
        print(math.gcd(v[x1],v[y1]))
