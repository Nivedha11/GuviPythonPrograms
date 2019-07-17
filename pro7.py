kn=int(input())
sm=0
for p in range(0,kn):
  if(pow(2,p)>kn):
    break
  sm=kn-pow(2,p)
print(sm)
