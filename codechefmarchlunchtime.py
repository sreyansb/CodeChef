from math import gcd

def findlcm(a):
    prod=a[0]
    for i in a:
        prod=(prod*i)//gcd(prod,i)
    return prod

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    k=findlcm(a)
    b=[k,0]
    pos=1
    for i in range(1,m+1):
        b[1]=i
        j=findlcm(b)
        if j>k:
            k=j
            pos=i
    print(pos)
            
