import math
for i in range(int(input())):
    setb=set()
    b=[]
    n=-1
    strings=[]
    flag=0
    for j in range(int(input())):
        ba,st=input().split()
        ba=int(ba)
        if ba!=-1:
            n=int(st,ba)
            setb.add(n)
            if len(setb)>1:
                    flag=1  
        else:
            strings.append(st)
    if n!=-1:
        if flag==0 and n<10**12:
            for i in strings:
                flag=1
                for j in range(int(max(i),36)+1,37):
                    if int(i,max(2,j))==n:
                        flag=0
                        break
                if flag==1:
                    break
        if flag==0 and n<10**12:
            print(n)
        else:
            print(-1)
    else:
        if flag==0:
            di={}
            for i in strings:
                if i not in di:
                    di[i]=set()
                for j in range(int(max(i),36)+1,37):
                    if int(i,max(2,j))>10**12:
                        break
                    di[i].add(int(i,max(2,j)))
                #print(di[i])
            k=di[strings[0]]
            for i in strings:
                k&=di[i]
            if len(k)!=0:
                print(min(k))
            else:
                print(-1)
        else:
            print(-1)
            
        
