"""
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]=abs(a[i])
    nosubs=0
    for i in range(len(a)):
        nosubs+=1 if a[i]&3!=2 else 0
        prod=a[i]
        for j in range(i+1,len(a)):
            prod*=a[j]
            nosubs+=1 if prod&3!=2 else 0
    print(nosubs)
"""
#linear soln
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]=abs(a[i])
        a[i]=a[i]&3
    #for each index i: n-i solns are possible.
    #totally n*(n+1)/2 solutions are possible.
    nosubs=0
    has2=0
    lastposof0=n
    lastposof2=n
    nosolnwith2=0#no solution, not number
    for i in range(n-1,-1,-1):
        if a[i]==0:
            nosubs+=n-i
            lastposof0=i
        elif a[i]==2:
            if lastposof0<lastposof2:
                nosolnwith2=lastposof0-i
            else:
                nosolnwith2=lastposof2-i
            nosubs+=n-i-nosolnwith2
            lastposof2=i
        else:
            if lastposof0<lastposof2:
                nosubs+=n-i
            else:
                nosubs+=n-i-nosolnwith2
        #print(nosubs)
    print(nosubs)          
     
    
        
    
    
            
        
            
        
