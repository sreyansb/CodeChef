for _ in range(int(input())):
    m,n=map(int,input().split())
    li=[[0 for i in range(m)] for j in range(n)]
    for i in range (m):
        li[i]=list(map(int,input().split()))
    total=n*m
    for i in range(1,m):
        for j in range (1,n):
            i1=1
            while(i-i1>=0 and i+i1<m and j-i1>=0 and j+i1<n):
                if (li[i-i1][j]==li[i+i1][j] and li[i][j-i1]==li[i][j+i1]):
                    total+=1
                    i1+=1
                else:
                    break
    print(total)
