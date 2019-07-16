N=int(input())
s1=input(" ")
s1=list(s1.split(' '))
c={}
for i in s1:
   if i in c:
      c[i]+=1
   else:
      c[i]=1
for key,value in c.items():
  if value==1:
     print(key)
