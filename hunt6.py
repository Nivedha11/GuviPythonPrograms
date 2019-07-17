nk=int(input())
m=input("")
m=list(m.split(" "))
e=[]
for v in range(0,len(m)):
  for u in range(v+1,len(m)):
    if m[v]==m[u]:
      e.append(m[v])
if(len(e)==0):
  print("unique")
else:
  print(e[0])
