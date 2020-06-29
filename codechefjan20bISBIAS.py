n,q=map(int,input().split())
a=list(map(int,input().split()))
for i in range (q):
    l,r=map(int,input().split())
    if r-l==1:
        print("NO")
    else:
        if (a[l]>a[l-1] and a[r-2]>a[r-1]) or (a[l]<a[l-1] and a[r-2]<a[r-1]):
            print("YES")
        else:
            print("NO")
    



"""n,q=map(int,input().split())
a=[-1]*(n+2)
a[n+1]=10000000000
a[1:n+1]=list(map(int,input().split()))
s=[0]*(n+2)
s[1]=(a[2]-a[1])//abs(a[2]-a[1])
cur=s[1]
for i in range(2,n+1):
    k=(a[i]-a[i-1])//abs(a[i]-a[i-1])
    if (k!=cur):
        s[i]=k
        cur=k
for _ in range(q):
    l,r=map(int,input().split())
    if sum(s[l:r+1])==0:
        print("YES")
    else:
        print("NO")
"""

"""
n,q=map(int,input().split())
a=[-1]*(n+2)
a[n+1]=10000000000
a[1:n+1]=list(map(int,input().split()))

for _ in range(q):
    l,r=map(int,input().split())
    if sum(s[l:r+1])==0:
        print("YES")
    else:
        print("NO")
    

4 3
1 3 2 4
1 4
2 3
2 4"""


"""
n,q=map(int,input().split())
li=[-1]*(n+2)
li[1:n+1]=list(map(int,input().split()))
li[0]=li[1]-li[2]
li[n+1]=li[n]-li[n-1]
for _ in range(q):
    l,r=map(int,input().split())
    noi=0
    nod=0
    conti=0
    contd=0
    for i in range(l,r+1):
        if li[i]>li[i-1]:
            if conti!=0:
                conti+=1
            if li[i]>li[i+1] and i<r:
                noi+=1
                conti=0
                contd+=1
            if contd==0 and i>l:
                contd+=1
        if li[i]<li[i-1]:
            if contd!=0:
                contd+=1
            if li[i]<li[i+1] and i<r:
                nod+=1
                contd=0
                conti+=1
            if conti==0 and i>l:
                conti+=1
    if nod==noi:
        print("YES")
    else:
        print("NO")
"""
