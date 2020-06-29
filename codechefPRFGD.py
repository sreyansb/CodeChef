for _ in range(int(input())):
    s=input()
    k,x=map(int,input().split())
    a=[0]*26
    i=0
    n=len(s)
    nof=0
    while(k>=0 and i<n):
        j=ord(s[i])-97
        a[j]+=1
        if a[j]>x:
            nof+=1
            k-=1
        i+=1
    print(i-nof)
        
    
        
        
