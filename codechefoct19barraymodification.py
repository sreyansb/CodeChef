"""for i in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    for i in range(k):
        li[j]=li[j]^li[n-1-(j)]
    print(*li)
    
for i in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    if k>1:
        if k%2==0:
            for i in range(k):
                j=i%n
                li[j]=li[j]^li[n-1-(j)]
                
                
            print(*li)
        else:
            for i in range(k):
                j=i%n
                li[j]=li[j]^li[n-1-(j)]
                
            
            print(*li)
    else:
        print(0)
    """
# cook your dish here
"""for i in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    #nop=k%nop
    #while(nop>-1):
    if k>1:
            while(k>n):
                j=k%n
                li[j]=li[j]^li[n-1-(j)]
                k=max(k//n,k%n)
                
                
            print(*li)
    else:
        print(0)"""
for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    flag=0
    if k>=n*3:
        flag=1
    k=k%(3*n)
    if k==0:
        k=3*n
    for i in range(k):
        j=i%n
        li[j]=li[j]^li[n-1-j]
    print(*li)
    

