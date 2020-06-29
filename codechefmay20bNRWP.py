for _ in range(int(input())):
    h,w,n=map(int,input().split())
    arr=[[0 for i in range(w+2)] for i in range(h+2)]
    for i in range(1,h+1):
        arr[i][1:w+1]=list(map(int,input().split()))
    
    parray=[[101 for i in range(w+2)] for i in range(h+2)]
    ppoints={}
    
    for i in range(n):
        r,c,p=map(int,input().split())
        ppoints[(r,c)]=0
        parray[r][c]=p

    sol=0
    def recurse(r,c):
        if r<1 or c<1:
            return 0
        if parray[r+1][c]!=101:
            rp1c=recurse(r+1,c)
        if ppoints[r-1][c][2]==0:
            recurse(r-1,c)
        if ppoints[r][c+1][2]==0:
            recurse(r,c+1)
        if ppoints[r][c-1][2]==0:
            recurse(r,c-1)
        ppoints[r][c][2]=-1 if (arr[r][c]<0 and parray[r][c]*arr[r][c]*-1>parray[r][c]*(parray[r+1][c]*ppoints"""

for _ in range(int(input())):
    h,w,n=map(int,input().split())
    arr=[[0 for i in range(w+2)] for i in range(h+2)]
    for i in range(1,h+1):
        arr[i][1:w+1]=list(map(int,input().split()))
    
    parray=[[0 for i in range(w+2)] for i in range(h+2)]
    ppoints=[]
    ppower=[1]*n
    for i in range(n):
        r,c,p=map(int,input().split())
        ppoints.append((r,c))
        parray[r][c]=p
    sol=0
    j=0
    for i in ppoints:
        k=arr[i[0]][i[1]]
        if k<0:
            parray[i[0]][i[1]]*=-1
            ppower[j]=-1
        j+=1
        sol+=k*parray[i[0]][i[1]]
    for i in sorted(ppoints,key=lambda x:(x[1],x[0]),reverse=True):
        sol+=parray[i[0]][i[1]]*parray[i[0]+1][i[1]]
        sol+=parray[i[0]][i[1]]*parray[i[0]][i[1]+1]
    print(sol)
    print(*ppower)
"""
"""
#worse 2nd attempt
for _ in range(int(input())):
    h,w,n=map(int,input().split())
    arr=[[0 for i in range(w+2)] for i in range(h+2)]
    for i in range(1,h+1):
        arr[i][1:w+1]=list(map(int,input().split()))
    
    parray=[[0 for i in range(w+2)] for i in range(h+2)]
    ppoints=[]
    
    for i in range(n):
        r,c,p=map(int,input().split())
        ppoints.append([r,c,1])
        parray[r][c]=p
    sol=0
    
    k=sorted(ppoints,key=lambda x:(x[1],x[0]),reverse=True)#sorting by (x[0],x[1]) gave wrong results
    for i in sorted(ppoints,key=lambda x:(x[1],x[0]),reverse=True):
        k=arr[i[0]][i[1]]
        if k<0:
            parray[i[0]][i[1]]*=-1
            i[2]=-1
        sol1=k*parray[i[0]][i[1]]
        sol2=parray[i[0]][i[1]]*parray[i[0]+1][i[1]]+parray[i[0]][i[1]]*parray[i[0]][i[1]+1]
        if sol1<abs(sol2) and k<0:
                parray[i[0]][i[1]]*=-1
                i[2]=1
                sol1=k*parray[i[0]][i[1]]
                sol2=parray[i[0]][i[1]]*parray[i[0]+1][i[1]]+parray[i[0]][i[1]]*parray[i[0]][i[1]+1]
        sol+=sol1+sol2                
        #print(i,sol)

    #print(parray)  
    print(sol)
    for i in ppoints:
        print(i[2],end=" ")
    print()
"""
"""adjacentpairs={}
    for i in range(1,h):
        for j in range(1,w):
            if parray[i][j]:
                adjacentpairs[(i,j)]=[]
                if parray[i+1][j]:
                    adjacentpairs[(i,j)].append((i+1,j))
                if parray[i][j+1]:
                    adjacentpairs[(i,j)].append((i,j+1))
"""

    
               
            
