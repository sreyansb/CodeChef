import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for z in range(int(input())):
        l,r=map(int,input().split())
        k=a[l-1:r]
        di={}
        for i in k:
            if i not in di:
                di[i]=0
            di[i]+=1
        x=0
        for i in di:
            x^=di[i]
        nos=0
        for i in di:
            j=di[i]^x
            if j<di[i]:
                nos+=math.factorial(di[i])//(math.factorial(j)*math.factorial(di[i]-j))
        print(nos%998244353)
        
        
            
        
            
            
