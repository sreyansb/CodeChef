for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    di={}
    lek=0
    for i in a:
        if i not in di:
            di[i]=0
            lek+=1
        di[i]+=1
    if len(set(di.values()))==lek:
        print("YES")
    else:
        print("NO")
    
