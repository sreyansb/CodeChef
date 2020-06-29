for _ in range(int(input())):
    n,q=map(int,input().split())
    a=[0]
    a+=list(map(int,input().split()))
    for z in range(q):
        x1,x2,y=map(int,input().split())
        nos=0
        prev=a[x1]
        for i in range(x1+1,x2+1):
            if prev>=a[i] and prev>=y and a[i]<=y:
                nos+=1
            elif prev<=a[i] and prev<=y and a[i]>=y:
                nos+=1
            prev=a[i]
        print(nos)
                
                
            
            
        
        
    
    
                
            
    
