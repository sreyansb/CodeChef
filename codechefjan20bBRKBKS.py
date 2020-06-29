for _ in range(int(input())):
    s,w1,w2,w3=map(int,input().split())
    l=[w1,w2,w3]
    if s>=sum(l):
        print(1)
    else:
        nof=0
        su=0
        for i in l:
            if su+i<=s:
                su+=i
            else:
                su=i
                nof+=1
        print(nof+1)
        
