n=6100000
prime=[True for i in range(0,n+1)]
p=2
s=set()
while (p<=n):
    if prime[p]==True:
        s.add(p)
        for i in range(2*p,n+1,p):
            prime[i]=False
    p+=1

for _ in range(int(input())):
    print("yes")
    #n=int(input())
    #a=list(map(int,input().split()))
    
    
