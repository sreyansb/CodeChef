for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    sum1=0
    for i in range(n):
        sum1+=min(a[i],b[i])
    print(sum1)
