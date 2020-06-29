for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=a
    while(len(l)>=k):
        z=[]
        j=len(l)
        for i in range(0,j-j%k,k):
            z.append(sum(l[i:i+k]))
        z+=l[j-j%k:]
        l=z
    for i in l:
        print(i,end=" ")
    print()

