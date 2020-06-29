m=10**9+7
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    summtotal=0
    for i in range(n):
        summtotal+=max(0,a[i]-i)
        summtotal%=m
    print(summtotal)
