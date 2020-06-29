n=int(input())
arr=[]
arr.append((1,n))
visited=[0]*(n+1)
while(len(arr)):
    arr1=arr[-1]
    arr.pop()
    low=arr1[0]
    high=arr1[1]
    mid=(low+high)//2
    if visited[mid]:
        continue
    print(mid)
    c1=input()
    visited[mid]=1
    if c1=='E':
        break
    elif c1=='L':
        nmid=(mid+1+high)//2
        if visited[nmid]:
            continue
        if nmid>n:
            continue
        print(nmid)
        c2=input()
        visited[nmid]=1
        if c2=='E':
            break
        elif c2=='L':
            if low<=nmid-1 and (low,nmid-1) not in arr and nmid-1!=high:
                arr.append((low,nmid-1))
            elif low<=nmid-1:
                arr.append((low,low))
        else:
            if low<=mid-1:
                arr.append((low,mid-1))
            else:
                arr.append((low,low))
            if nmid+1<=high:
                arr.append((nmid+1,high))
            else:
                arr.append((high,high))
            """
            nmid2=(low+mid-1)//2
            print(nmid2)
            c3=input()
            if c3=='E':
                break
            elif c3=='L':
                if low<=nmid2-1 and (low,nmid2-1) not in arr and nmid2-1!=high:
                    arr.append((low,nmid2-1))
                elif low<=nmid2-1:
                    arr.append((low,low))
                if nmid+1<=high and (nmid+1,high) not in arr and nmid+1!=low:
                    arr.append((nmid+1,high))
                elif nmid+1<=high:
                    arr.append((high,high))
                    
            else:
                if nmid2+1<=mid-1:
                    arr.append((nmid2+1,mid-1))
                if nmid+1<=high and (nmid+1,high) not in arr and nmid+1!=low:
                    arr.append((nmid+1,high))
                elif nmid+1<=high:
                    arr.append((high,high))
            """
    else:
        nmid=(mid-1+low)//2
        if visited[nmid]:
            continue
        if nmid<1:
            continue
        print(nmid)
        c2=input()
        visited[nmid]=1
        if c2=='E':
            break
        elif c2=='G':
            if nmid+1<=high and (nmid+1,high) not in arr and nmid+1!=low:
                arr.append((nmid+1,high))
            elif nmid+1<=high:
                arr.append((high,high))
        else:
            if mid+1<=high:
                arr.append((mid+1,high))
            else:
                arr.append((high,high))
            if low<=nmid-1:
                arr.append((low,nmid-1))
            else:
                arr.append((low,low))
    
            """
            nmid2=(high+mid+1)//2
            print(nmid2)
            c3=input()
            if c3=='E':
                break
            elif c3=='G':
                if low<=nmid-1:
                    arr.append((low,nmid-1))
                if nmid2+1<=high and (nmid2+1,high) not in arr and nmid2+1!=low:
                    arr.append((nmid2+1,high))
                elif nmid2+1<=high:
                    arr.append((high,high))
            else:
                if mid+1<=nmid2-1:
                    arr.append((mid+1,nmid2-1))
                if low<=nmid-1 and (low,nmid-1) not in arr and nmid-1!=high: 
                    arr.append((low,nmid-1))
                elif low<=nmid-1:
                    arr.append((low,low))
            """
    print(arr)
"""n=int(input())
arr=[]
arr.append((1,n))
while(len(arr)):
    arr1=arr[-1]
    arr.pop()
    low=arr1[0]
    high=arr1[1]
    mid=(low+high)//2
    print(mid)
    c1=input()
    if c1=='E':
        break
    elif c1=='L':
        nmid=(mid+1+high)//2
        print(nmid)
        c2=input()
        if c2=='E':
            break
        elif c2=='L':
            if low<=nmid-1 and (low,nmid-1) not in arr:
                arr.append((low,nmid-1))
            elif low<=nmid-1:
                arr.append((low,low))
        else:
            nmid2=(low+mid-1)//2
            print(nmid2)
            c3=input()
            if c3=='E':
                break
            elif c3=='L':
                if low<=nmid2-1 and (low,nmid2-1) not in arr:
                    arr.append((low,nmid2-1))
                else:
                    arr.append((low,low))
                if nmid+1<=high and (nmid+1,high) not in arr:
                    arr.append((nmid+1,high))
                elif nmid+1<=high:
                    arr.append((high,high))
            else:
                if nmid2+1<=mid-1:
                    arr.append((nmid2+1,mid-1))
                if nmid+1<=high and (nmid+1,high) not in arr:
                    arr.append((nmid+1,high))
                elif nmid+1<=high:
                    arr.append((high,high))
    else:
        nmid=(mid-1+low)//2
        print(nmid)
        c2=input()
        if c2=='E':
            break
        elif c2=='G':
            if nmid+1<=high and (nmid+1,high) not in arr:
                arr.append((nmid+1,high))
            elif nmid+1<=high:
                arr.append((high,high))
        else:
            nmid2=(high+mid+1)//2
            print(nmid2)
            c3=input()
            if c3=='E':
                break
            elif c3=='G':
                if low<=nmid-1:
                    arr.append((low,nmid-1))
                if nmid2+1<=high and (nmid2+1,high) not in arr:
                    arr.append((nmid2+1,high))
                elif nmid2+1<=high:
                    arr.append((high,high))
            else:
                if mid+1<=nmid2-1:
                    arr.append((mid+1,nmid2-1))
                if low<=nmid-1 and (low,nmid-1) not in arr: 
                    arr.append((low,nmid-1))
                elif low<=nmid-1:
                    arr.append((low,low))"""
    
                
    

"""
n=int(input())
arr=[]
arr.append((1,n))
while(len(arr)):
    arr1=arr[-1]
    arr.pop()
    low=arr1[0]
    high=arr1[1]
    mid=(low+high)//2
    print(mid)
    c1=input()
    if c1=='E':
        break
    elif c1=='L':
        nmid=(mid+1+high)//2
        print(nmid)
        c2=input()
        if c2=='E':
            break
        elif c2=='L':
            print(1)
            c3=input()
            if c3=='E':
                break
            if c3=='L':
                if low<=mid-1:
                    arr.append((low,mid-1))
            else:
                if low<=nmid-1:
                    arr.append((low,nmid-1))
        else:
            nmid2=(low+mid-1)//2
            print(nmid2)
            c3=input()
            if c3=='E':
                break
            elif c3=='L':
                if low<=nmid2-1:
                    arr.append((low,nmid2-1))
                if nmid+1<=high:
                    arr.append((nmid+1,high))
            else:
                if nmid2+1<=mid-1:
                    arr.append((nmid2+1,mid-1))
                if nmid+1<=high:
                    arr.append((nmid+1,high))
    else:
        nmid=(mid-1+low)//2
        print(nmid)
        c2=input()
        if c2=='E':
            break
        elif c2=='G':
            print(1)
            c3=input()
            if c3=='E':
                break
            if c3=='L':
                if mid+1<=high:
                    arr.append((mid+1,high))
            else:
                if nmid+1<=high:
                    arr.append((nmid+1,high))
            
        else:
            nmid2=(high+mid+1)//2
            print(nmid2)
            c3=input()
            if c3=='E':
                break
            elif c3=='G':
                if low<=nmid-1:
                    arr.append((low,nmid-1))
                if nmid2+1<=high:
                    arr.append((nmid2+1,high))
            else:
                if mid+1<=nmid2-1:
                    arr.append((mid+1,nmid2-1))
                if low<=nmid-1:
                    arr.append((low,nmid-1))
    
    print(arr) 
"""       
        
            
            
"""n=int(input())
visited=[0]*(n+1)
arr=[(1,n)]
while(len(arr)!=0):
    arr1=arr[0]
    arr.pop(0)
    mid1=(arr1[0]+arr1[1])//2
    
    print(mid1)
    ch1=input()
    visited[mid1]=1
    if ch1=='E':
        break
    elif ch1=='L':
        s1=mid1+1
        e1=arr1[1]
        nmid=(s1+e1)//2
        
        print(nmid)
        ch2=input()
        visited[nmid]=1
        if ch2=='E':
            break
        elif ch2=='G':
            if arr1[0]<=mid1-1:
                arr.append((arr1[0],mid1-1))
            if(nmid+1<=e1):
                arr.append((nmid+1,arr1[1]))
        else:
            if arr1[0]<=mid1-1:
                arr.append((arr1[0],mid1-1))
            if(nmid+1<=e1):
                arr.append((mid1+1,nmid-1))
    else:
        s1=arr1[0]
        e1=mid1-1
        nmid=(s1+e1)//2
        
        print(nmid)
        ch2=input()
        visited[nmid]=1
        if ch2=='E':
            break
        elif ch2=='G':
            if nmid+1<=mid1+1:
                arr.append((nmid+1,mid1+1))
            if(mid1+1<=arr1[1]):
                arr.append((mid1+1,arr1[1]))
        else:
            if arr1[0]<=nmid-1:
                arr.append((arr1[0],nmid-1))
            if(mid1+1<=arr1[1]):
                arr.append((mid1+1,arr1[1]))
"""
"""
n=int(input())
low=1
#visited=[0]*(n+1)
arr=[(1,n)]
while(len(arr)!=0):
    arr1=arr[0]
    low=arr1[0]
    n=arr1[1]
    arr.pop(0)
    mid=low+(n-low)//2
    if mid==0:
        continue
    print(mid)
    k1=input()
    if k1=='E':
        break
    else:
        if mid-1==0:
            arr.append((n,n))
            continue
        print(mid-1)
        k2=input()
        if k2=='E':
            break
        if k1==k2:
            if k1=='L':
                if low<=mid-2:
                    arr.append((low,mid-2))
            else :
                if mid+1<=n:
                    arr.append((mid+1,n))
        else:
            #either LG or GL for mid and mid-1
            #Assuming truth is lesser than mid=>lesser than mid-1
            if low<=mid-2:
                arr.append((low,mid-2))
            if mid+1<=n:
                arr.append((mid+1,n))
    #print(arr)
"""
"""n=int(input())
low=1
#visited=[0]*(n+1)
arr=[(1,n)]
visited=[0]*(n+1)
while(len(arr)!=0):
    arr1=arr[0]
    low=arr1[0]
    n=arr1[1]
    arr.pop(0)
    mid=low+(n-low)//2
    print(mid)
    visited[mid]=1
    k1=input()
    if k1=='E':
        break
    elif k1=='L':
        nmid=(mid+1+n)//2
        print(nmid)
        visited[nmid]=1
        k2=input()
        if k2=='E':
            break
        elif k2=='G':
            if low<=mid-1:
                arr.append((low,mid-1))
            if nmid+1<=n:
                arr.append((mid+1,n))
        else:
            if low<=mid-1:
                arr.append((low,mid-1))
    else:
        nmid=(low+mid-1)//2
        print(nmid)
        visited[nmid]=1
        k2=input()
        if k2=='E':
            break
        elif k2=='G':
            if mid+1<=n:
                arr.append((mid+1,n))
        else:
            if low<=mid-1:
                arr.append((low,mid-1))
            if mid+1<=n:
                arr.append((mid+1,n))
    #print(arr)
"""
"""
    elif k=='L':
        print(mid-1)
        l=input()
        if l=='E':
            break
        elif l==k:
            n=mid-2
        else:
            print(1)
            z=input()
            if z=='E':
                break
            elif z=='L':
                low=mid+1
            else:
                low=mid+1
    else:
        print(mid+1)
        l=input()
        if l=='E':
            break
        elif l==k:
            low=mid+2
        else:
            print(mid+1)
            z=input()
            if z=='G':
                low=mid+2
            else:
                n=mid-1
    """
    
            
    
"""n=int(input())
print(1)
k=input()
option=0
if k=='E':
    option=-1
elif k=='L':
    option=1
if option>-1:
    print(1)
    input()
    low=1
    while(low<=n):
        mid=(low+n)//2
        print(mid)
        k=input()
        if k=='E':
            break
        #print("k",k)
        if option==0:
            if k=='G':
                low=mid+1
            elif k=='L':
                n=mid-1
            else:
                #print(mid,"broken here")
                break
            print(mid)
            input()
        else:
            print(mid)
            k=input()
            if k=='G':
                low=mid+1
            elif k=='L':
                n=mid-1
            else:
                break
    #print("low=",low,mid)
"""                   
            
            
            
            
                
                    
                
                
            
                
            
            
        
        
    
                
            
    
    
    
    
