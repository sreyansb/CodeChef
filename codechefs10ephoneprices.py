for i in range(int(input())):
    n=int(input())
    s=[751]*(n+5)
    s[5:]=list(map(int,input().split()))
    count=0
    for i in range(4,n+5):
        if s[i]<min(s[i-1],s[i-2],s[i-3],s[i-4],s[i-5]):
            count+=1
    print(count)
