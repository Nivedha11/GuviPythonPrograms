k1=int(input())
n1=list(map(int, input().split()))
l=int(len(n1)/2)
if sum(n1[:l])//len(n1[:l]) == sum(n1[l:])//len(n1[l:]):
    print('yes')
else:
    print('no')
