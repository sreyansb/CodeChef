n,q=map(int,input().split())
li=[-1]*(n+2)
li[n+1]=10000000000
li[1:n]=list(map(int,input().split()))
for _ in range(q):
    l,r=map(int,input().split())
    l0=li
