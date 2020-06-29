t=input().split()
t=int(t[0])
for i in range (t):
    s=list(map(int,input().split()))
    k=list(map(int,input().split()))
    m=set(k)
    if (len(m)!=s[2]):
        print(-1)
    else:
        print(len(m))
            
