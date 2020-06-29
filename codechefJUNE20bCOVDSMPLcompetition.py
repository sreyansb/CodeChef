for _ in range(int(input())):
    n,p=map(int,input().split())
    a=[[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,1+n):
        for j in range(1,1+n):
            s="1 "+str(i)+" "+str(j)+" "+str(i)+" "+str(j)+"\n"
            x=int(input(s))
            a[i][j]=x
    print(2)
    for i in a[1:]:
        print(*i[1:])
        
