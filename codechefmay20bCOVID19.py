for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mini=100000000
    maxi=1
    for i in range(n):
        mi=1
        for j in range(i-1,-1,-1):
            diff=a[j+1]-a[j]
            if diff>2:
                break
            mi+=1
        for j in range(i+1,n):
            diff=a[j]-a[j-1]
            if diff>2:
                break
            mi+=1
        mini=min(mini,mi)
        maxi=max(maxi,mi)
    print(mini,maxi)
        
    
