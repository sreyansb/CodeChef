
def send(n,k):
    no=0
    while(n%2==0):
        no+=1
        n=n//2
    for i in range(3,int(n**0.5)+1,2):
        while(n%i==0):
            no+=1
            n//=i
    if n>2:
        no+=1
    return 1 if no>=k else 0    
for _ in range(int(input())):
    x,k=map(int,input().split())
    if k==1 and x>=2:
        print(1)
    else:
        print(send(x,k))

"""
#GIVES TLE
def send(x,k):
    i=2
    initial=i**k
    new=i**(k-1)*(i+1)
    while(x>initial):
        initial=new
        new=(new//i)*(i+1)
        if (new%i!=0):
            i+=1
    return (1 if x==initial else 0)
    
for _ in range(int(input())):
    x,k=map(int,input().split())
    ans=send(x,k)
    print(ans)
"""
