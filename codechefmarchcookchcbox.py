for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=max(a)
    k=0
    j=0
    for i in range(n):
        if c==a[i]:
            k=i
    for i in range(n-1,-1,-1):
        if c==a[i]:
            j=i
    dist=n//2-(k-j)
    if dist>=0:
        print(dist)
    else:
        print(0)
    
        
        
