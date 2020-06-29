import math
for _ in range(int(input())):
    l,r=map(int,input().split())
    if r<l:
        l,r=r,l
    nosq=math.floor(r**0.5)-math.ceil(l**0.5)+1
    print(r-l+1-nosq)
