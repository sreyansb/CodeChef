'''n,t=map(int,input().split())
a=list(map(int,input().split()))
k=[0]*n
p=[0]*(10**5+1)
k[n-1]=1
p[a[n-1]]=1
for  i in range(n-2,-1,-1):
    if p[a[i]]==0:
        k[i]=k[i+1]+1
        p[a[i]]=1
    else:
        k[i]=k[i+1]
print(k)
'''
def countoccur(arr, x, n): 
    i = left(arr, 0, n-1, x, n) 
    if i == -1: 
        return i 
    j = right(arr, i, n-1, x, n);       
    return j-i+1; 
  
def left(arr, low, high, x, n): 
    if high >= low: 
        mid = (low + high)//2
    else:
        return -1
    if (mid == 0 or x > arr[mid-1]) and arr[mid] == x: 
        return mid 
    elif x > arr[mid]: 
        return left(arr, (mid + 1), high, x, n) 
    else: 
        return left(arr, low, (mid -1), x, n) 
    return -1; 
def right(arr, low, high, x, n): 
    if high >= low: 
        mid = (low + high)//2
    else:
        return -1
    if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x : 
        return mid 
    elif x < arr[mid]: 
        return right(arr, low, (mid -1), x, n) 
    else: 
        return right(arr, (mid + 1), high, x, n)      
    return -1
n,t=map(int,input().split())
a=list(map(int,input().split()))
for i in range(int(input())):
    sol="Champion"
    c,b=map(int,input().split())
    x=a[c-1:b]
    for i in set(x):
        o=countoccur(x,i,b-c+1)
        if o>(b-c+1)/2.0:
            sol=i
            break
    print(sol)
