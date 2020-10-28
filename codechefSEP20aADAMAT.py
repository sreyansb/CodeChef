for _ in range(int(input())):
    n=int(input())
    grid=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        grid[i][1:]=list(map(int,input().split()))
        
    def transpose(l):
        for i in range(1,l+1):
            for j in range(1,i):
                grid[i][j],grid[j][i]=grid[j][i],grid[i][j]

    no=0
    for i in range(n,1,-1):
        for j in range(1,i):
            #print(grid[i][j],i-1,j,n,(i-1)*n+j)
            if grid[i][j]!=((i-1)*n+j):
                transpose(i)
                #print(grid)
                no+=1
    print(no)
