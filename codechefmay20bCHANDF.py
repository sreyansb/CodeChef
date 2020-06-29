from math import log2
for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
    if x==0 or y==0:
        print(l)
    else:
        ans=x|y
        if ans>=l and ans<=r:
            pass
        elif ans>r:
            sol=""
            k=0
            ansbin=bin(ans)[2:]
            for i in range(len(ansbin)-1,-1,-1):
                sol=ansbin[i]+sol
            ans=int(sol,2)
        print(ans)
                    
                
                           
"""
for i in range(6,201):
    for j in range(1,30):
        print(bin(i)[2:],bin(j)[2:])
        maxi=0
        for k in range(1,(i|j)+1):
            s=(i&k)*(j&k)
            if s>maxi:
                maxi=s
                print("maxl",k,bin(k&(i|j))[2:])
        print()

"""         
"""from math import log2
for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
    if x==0 or y==0:
        ans=0
    else:
        ans=x|y
        maxi=-1
        index=-1
        for i in range(l,r+1):
            z=(x&i)*(y&i)
            if maxi<z:
                maxi=z
                index=i
        ans=index
    print(ans)
"""
"""
for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
"""

"""
#15 points ka partial answer
for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
    if x==0 or y==0:
        ans=0
    else:
        ans=x|y
    print(ans)
"""

"""for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
    if x==0 or y==0:
        bestans=0
    else:
        ans=x|y
        bestans=x|y
        while(ans>r or ans<l):
            ansinside=(r+l)>>1
            
            
    print(bestans)
"""

"""
i=1
j=15
maxi=-1
index=-1
for k in range(0,64):
    z=(i&k)*(j&k)
    if maxi<z:
        maxi=z
        index=k
    #print(k,z)
print(index)
print("hello")
"""
"""
for i in range(200):
    for j in range(200):
        index=-1
        maxi=0
        for k in range(0,1000):
            z=(i&k)*(j&k)
            if maxi<z:
                maxi=z
                index=k
            #print(k,z)
        k=(index==(i|j))
        if k==0:
            print(i,j)
print("end")
"""
