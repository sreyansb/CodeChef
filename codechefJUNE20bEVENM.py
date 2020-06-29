for _ in range(int(input())):
    n=int(input())
    start=1
    rev=0
    final_matrix=[]
    while(start<=n*n):
        if rev==0:
            final_matrix.append(list(range(start,start+n)))
        else:
            final_matrix.append(list(range(start+n-1,start-1,-1)))
        start+=n
        rev^=1
    for i in final_matrix:
        print(*i)
        
