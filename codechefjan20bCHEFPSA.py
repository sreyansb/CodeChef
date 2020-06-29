import math
for _ in range(int(input())):
    n=int(input())
    a2n=list(map(int,input().split()))
    """
Let Sk denote a suffix sum.
Therefore P(n-k) is a corresponding prefix sum.
Sk+P(n-k)==Sum of the the required array of length n.
Total number of such pairs=(n-1)
Therefore the remaining two elements in the array of length 2n should be the sum itself.
If the sum of suffix-prefix array is (Sum of array of length n)*(n+1)
"""
    k=sum(a2n)/(n+1)
    if k!=int(k):
        print(0)
    else:
        di={}
        flag=0
        res=math.factorial(n-1)
        for i in a2n:
            if i!=k:
                if i not in di:
                    di[i]=0
                di[i]+=1
        for i in di:
            if k-i in di:
                if k!=2*i:
                    if di[i]==di[k-i]:
                        res*=2*di[i]
                        di[k-i]=1
                    else:
                        res=0
                        break
                else:
                    if di[i]%2==1:
                        res=0
                        break
                    
                        
                
                    
                    
                
        
