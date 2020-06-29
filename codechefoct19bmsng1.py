import math
for i in range(int(input())):
    setb=set()
    b=[]
    n=0
    strings=[]
    values=[]
    flag=0
    for j in range(int(input())):
        ba,st=input().split()
        ba=int(ba)
        if ba!=-1:
            n=int(st,ba)
            setb.add(n)
            if len(setb)>1:
                flag=1
                break
        else:
            b.append(ba)
            strings.append(st)
        print("NO")
