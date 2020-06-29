from math import sqrt
for _ in range(int(input())):
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    p=[]
    xpos=[]
    xneg=[]
    ypos=[]
    yneg=[]
    dix=[0]*100005
    diy=[0]*100005
    zx=0
    zy=0
    for i in x:
        if i<0:
            xneg.append(i)
        elif i>0:
            xpos.append(i)
        else:
            zx=1
        dix[abs(i)]+=1
    for i in y:
        if i<0:
            yneg.append(i)
        elif i>0:
            ypos.append(i)
        else:
            zy=1
        diy[abs(i)]+=1
    no=0
    if zx:
        no=(n-1)*m
    if zy :
        no=(m-1)*n
    if zx and zy:
        no=(m-1)*(n-1)
        
    for i in xpos:
        for j in xneg:
            height=sqrt((i*(-j)))
            #this part
            if height!=int(height):
                continue
            height=int(height)
            try:
                no+=diy[height]
            except:
                continue
    for i in ypos:
        for j in yneg:
            height=sqrt((i*(-j)))
            #this part
            if height!=int(height):
                continue
            height=int(height)
            try:
                no+=dix[height]
            except:
                continue
    print(no)
            
