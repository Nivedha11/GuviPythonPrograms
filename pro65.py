k,n = map(int,input().split())
u1 = list(map(int,input().split()))
v1 = int(input())
w = (sum(u1)-u1[n])//2
if v1==w:
  print("Bon Appetit")
else:
  print(v1-w)
