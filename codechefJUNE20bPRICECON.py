for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dif=0
    for i in a:
        dif+=max(0,i-k)
    print(dif)
                 
