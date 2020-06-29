for i in range(int(input())):
    k=[0]*10
    for j in range(int(input())):
        s=input()
        for i in range(10):
            if s[i]=='1' and k[i]==0:
                k[i]=1
            elif s[i]=='1' and k[i]==1:
                k[i]=0
    
            
print(k.count(1))
    
