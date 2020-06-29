#VERY NICE PROBLEM
from math import ceil
from math import floor
for _ in range(int(input())):
  n,p=map(int,input().split())
  a=list(map(int,input().split()))
  flag=1
  finalsol=[0]*n
  for i in range(n):
    if flag==0:
      break
    if p%a[i]!=0:
      finalsol[i]=int(ceil(p/a[i]))
      flag=0
    else:
      for j in range(i+1,n):
        if p%a[j]!=0:
          finalsol[j]=int(ceil(p/a[j]))
          flag=0
          break
        else:
          if (p-a[i])%a[j]!=0 and (p-a[j])%a[i]!=0:
            flag=0
            h=max(a[j],a[i])
            z=min(a[j],a[i])
            if h==a[j]:
              maxpos=j
              minpos=i
            else:
              maxpos=i
              minpos=j
            k=(p-h)
            finalsol[maxpos]=1
            finalsol[minpos]=int(ceil(k/z))
            break
  if flag==0:
    print("YES",*finalsol)
  else:
    print("NO")
"""
def factors(n):
  fact={1,n}
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      fact.add(i)
      fact.add(n//i)
  return fact
for _ in range(int(input())):
  n,p=map(int,input().split())
  a=list(map(int,input().split()))
  g=factors(p)
  k=set(a)-g
  if len(k)==0:
    print("NO")
  else:
    print("YES",end=" ")
    finalsol=[0]*n
    for i in range(n):
      if a[i] not in g:
        if a[i]>p:
          finalsol[i]=1
          break
        else:
          finalsol[i]=p//a[i]-1
          p=p-p%a[i]-a[i]
    print(*finalsol)
"""
      
  
  
          
          
      
