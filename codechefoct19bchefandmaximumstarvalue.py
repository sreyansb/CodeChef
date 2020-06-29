"""
for i in range(int(input())):
    z=int(input())
    l=list(map(int,input().split()))
    di={0:0}
    curmax=0
    if z>1:
        for i in range(1,z):
            k=range(i-1,-1,-1)
            j=l[i]
            di[i]=0
            for h in k:
                if l[h]%j==0:
                    di[i]+=di[h]+1
                    if di[h]==curmax:
                        break
            curmax=max(curmax,di[i])
    print(curmax)
    """
"""
for i in range(int(input())):
    z=int(input())
    l=list(map(int,input().split()))
    di={0:0}
    for i in range(1,z):
        k=l[0:i]
        j=l[i]
        di[i]=len([b for b in k if b%j==0])
    
    print(di[sorted(di,key=lambda x:di[x])[-1]])"""
# cook your dish here
for i in range(int(input())):
    z=int(input())
    li=list(map(int,input().split()))
    di={0:set()}
    maxv=0
    for i in range(1,z):
        di[i]=set()
        for j in di:
            if li[j]%li[i]==0 and j!=i:
                 di[i]=di[i]|di[j]|{j}
                
                    
        maxv=max(len(di[i]),maxv)
        print(di)
    print(maxv)
        
