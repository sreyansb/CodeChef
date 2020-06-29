for _ in range(int(input())):
    n,k=map(int,input().split())
    cost=list(map(int,input().split()))
    finalans=[-1]*n
    for i in range(n-1,-1,-1):
        finalans[i]=cost[i]
        if i+k<n:
            finalans[i]+=finalans[i+k]
    print(max(finalans))
    
