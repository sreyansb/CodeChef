"""def calcbn(b1,b2):
    b1=format(b1,'030b')
    b2=format(b2,'030b')
    no=1
    for i in range(30):
        if b1[i]=='1' and b2[i]=='1':
                no*=2
    return no
    
for _ in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    a=[1]*n
    nof=1
    for i in range(1,n):
        a[i]=calcbn(b[i],b[i-1])
        nof*=a[i]
    print(nof%(10**9+7))"""
def calcbn(b1,b2):
    no=1
    while(b1 and b2):
        if b2%2:
            if b1%2:
                no<<=1
            else:
                no=0
                break
        b1>>=1
        b2>>=1
    return no
k=10**9+7
for _ in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    a=[1]*n
    nof=1
    for i in range(1,n):
        a[i]=calcbn(b[i],b[i-1])
        nof=((nof%k)*(a[i]%k))%k
    print(nof)
