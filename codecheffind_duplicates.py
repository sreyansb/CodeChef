s=list(input())
for _ in range(int(input())):
    query=input().split()
    q=int(query[0])
    l=int(query[1])
    if q==1:
        char=query[2]
        s[l-1]=char
    else:
        r=int(query[2])
        k=s[l-1:r]
        k.sort()
        count=0
        
        print(count)
            
        
            
