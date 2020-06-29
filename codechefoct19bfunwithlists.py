# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(range(0,10**n,k))
    di={0}
    for i in l:
        if int(str(i)[::-1]) in l and i not in di:
            di.add(i)
            di.add(int(str(i)[::-1]))
    print(len(di)%((10**9)+7))
