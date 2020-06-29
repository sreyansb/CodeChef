for _ in range(int(input())):
    n=int(input())
    li=[0,0,0,0]
    a=list(map(int,input().split()))
    sol="YES"
    for i in a:
        if i==5:
            li[1]+=1
        elif i==10:
            if li[1]>0:
                li[2]+=1
                li[1]-=1
            else:
                sol="NO"
                break
        else:
            if li[2]>0:
                li[2]-=1
                li[3]+=1
            elif li[1]>1:
                li[1]-=2
                li[3]+=1
            else:
                sol="NO"
                break
    print(sol)
                
        
