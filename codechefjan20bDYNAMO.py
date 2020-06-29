for _ in range(int(input())):
    n=int(input())
    a=int(input())
    s=2*(10**n)
    print(s+a)
    b=int(input())
    s-=b
    c=int(10**n-1)-b
    print(c)
    s-=c
    d=int(input())
    s-=d
    print(s)
    k=int(input())
    if k==-1:
        break
        
        
