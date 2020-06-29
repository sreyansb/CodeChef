for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans="YES"
    if n<7 and a.count(1)>1:
        ans="NO"
    elif n<7 and a.count(1)<=1:
        ans="YES"
    else:
        for i in range(n-5):
            k=a[i:i+6]
            if k.count(1)>1:
                ans="NO"
                break
    print(ans)
                
            
                
                    
