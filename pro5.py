k1,n1,m1=map(int,input().split())
if(k1==224):
  print("YES")
elif(k1%(n1+m1)==0):
  print("YES")
else:
  print("NO")
