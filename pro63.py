kn=input()
N=[]
for v in kn:
    if v not in N:
        N.append(v)
        
    else:
        break
print(len(N))
