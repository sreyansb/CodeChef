for _ in range(int(input())):
    n,m=map(int,input().split())
    edges=[]
    for i in range(m):
        a,b=map(int,input().split())
        edges.append((a,b))
    if m%2==0:
        answ=-1
        for i in range(m):
            print(answ)
            answ*=-1
    else:
        ans=[0]
        print(0)
        answ=-1
        for i in range(1,m):
            print(answ)
            answ*=-1
    
        
        
