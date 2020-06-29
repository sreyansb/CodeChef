"""
[[1, 0, 1, 0], [0, 0, 2, 3], [0, 2, 0, 1], [2, 0, 0, 0]]
[[0, 0, 3, 0], [0, 2, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
[[0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
"""        
sumtotal=0
for _ in range(int(input())):
    total=0
    a=[[0 for i in range(4)] for j in range(4)]
    n=int(input())
    for i in range(n):
        ch,value=input().split()
        ch=ord(ch)-ord('A')
        value=int(value)//3
        a[ch][value-1]+=1
    value=100
    s=[]
    for i in range(4):
        for j in range(4):
            if i==j:
                continue
            for k in range(4):
                if k==j or k==i:
                    continue
                for l in range(4):
                    if l==k or l==j or l==i:
                        continue
                    s.append([a[0][i],a[1][j],a[2][k],a[3][l]])
    maxval=-400
    for i in s:
        value=100
        netval=0
        k=sorted(i,reverse=True)
        for j in k:
            if j==0:
                netval-=100
            else:
                netval+=j*value
                value-=25
        maxval=max(maxval,netval)
    sumtotal+=maxval
    print(maxval)        
print(sumtotal)





"""char_list=[]
    pos_list=[]
    for i in range(4):
        maxi=0
        maxpos,character=0,0
        for j in range(4):
            if j not in char_list:
                k=max(a[j])
                maxi=max(maxi,k)
                if maxi==k:
                    maxpos=a[j].index(maxi)
                    character=j
        char_list.append(character)
        total+=value*maxi
        value-=25
        if maxi==0 or maxpos in pos_list:
            total-=100*(4-i)
            break
        pos_list.append(maxpos)"""
        
    

