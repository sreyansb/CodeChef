a=[0]*129
for i in range(2,129):
    k=a[i-2::-1]
    l=len(k)
    if a[i-1] in k:
        k=k.index(a[i-1])
        a[i]=i-(l-k)
    else:
        a[i]=0
for i in range(int(input())):
    n=int(input())
    print(a[:n].count(a[n-1]))
        
