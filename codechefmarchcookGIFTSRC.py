for _ in range(int(input())):
    n=int(input())
    s=input()
    if s[0]=='L':
        x,y=-1,0
    elif s[0]=='R':
        x,y=1,0
    elif s[0]=='U':
        x,y=0,1
    else:
        x,y=0,-1
    for i in range(1,n):
        if s[i]=='L':
            if s[i-1]=='D' or s[i-1]=='U':
                x-=1
        elif s[i]=='R':
            if s[i-1]=='D' or s[i-1]=='U':
                x+=1
        elif s[i]=='D':
            if s[i-1]=='R' or s[i-1]=='L':
                y-=1
        else:
            if s[i-1]=='R' or s[i-1]=='L':
                y+=1
    print(x,y)
            
        
