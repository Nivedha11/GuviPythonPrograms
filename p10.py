k,n=list(map(str,input().split()))
count=0
for i in range(0,len(k)):
    if(k[i]!=n[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
