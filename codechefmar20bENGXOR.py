def findParity(x): 
    y = x ^ (x >> 1) 
    y = y ^ (y >> 2)
    y = y ^ (y >> 4)
    y = y ^ (y >> 8) 
    y = y ^ (y >> 16) 
    if (y & 1): 
        return 1; 
    return 0; 
for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    oddparity=0
    for i in a:
        oddparity+=findParity(i)
    evenparity=n-oddparity
    for i in range(q):
        if(findParity(int(input()))):
            print(oddparity,evenparity)
        else:
            print(evenparity,oddparity)
    
    
        
        
        
            
