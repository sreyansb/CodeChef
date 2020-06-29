for _ in range(int(input())):
    n,m=map(int,input().split())
    fruittypes=list(map(int,input().split()))
    costmatrix=list(map(int,input().split()))
    fruity={}
    pos=0
    for i in range(1,m+1):
        fruity[i]=0
    for i in range(n):
        fruity[fruittypes[i]]+=costmatrix[i]
    mini=fruity[fruittypes[0]]
    for i in range(1,n):
        mini=min(mini,max(0,fruity[fruittypes[i]]))
    print(mini)
    
        
        
        
        
