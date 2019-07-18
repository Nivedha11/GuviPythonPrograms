k1 = int(input())
while k1%10==0:
    k1=k1//10
k1=str(k1)
n1=k1[::-1]
if k1==n1:
    print('yes')
else:
    print('no')
