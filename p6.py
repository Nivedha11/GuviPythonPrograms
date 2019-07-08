R1,R2=map(str,input().split())
if(len(R1)!=len(R2)):
   print("no")
else:
   S1=[R1.count(a) for a in R1]
   T1=[R2.count(a) for a in R2]
if(S1==T1):
   print("yes")
else:
   print("no")
