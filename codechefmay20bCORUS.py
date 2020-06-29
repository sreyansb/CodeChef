for _ in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    di={}
    for i in range(26):
        di[i]=0
    for i in s:
        di[ord(i)-97]+=1
    #print(di)
    listdi=sorted(di.values(),reverse=True)
    #print(listdi)
    for _1 in range(q):
        i=int(input())
        j=0
        sol=0
        while(listdi[j]>i):
            sol+=listdi[j]-i
            j+=1
        print(sol)
            
    
        
        
