from itertools import combinations
kn,pq = input().split()
pq = int(pq)
x = []
hj2 = combinations(kn,len(kn)-pq)
for a1 in hj2:
    x.append("".join(a1))
print(min(x))
