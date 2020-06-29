#question is not about leap year.It happens in FEB when the first friday appears
#on 6th or 7th
import math
import datetime 
import calendar
def leap(y):
    if (y%4==0 and y%100) or y%400==0:
        return 1
    return 0
def findday(y):
    return datetime.datetime(y,2,1).weekday()
a=[0]*2001
y2=2000
no=505
while(y2>=1):
    k=findday(y2)
    #means friday is on 7th.
    if k==5 :
        a[y2]=no
        no-=1
        y2-=1
    #Means friday is on 6th.
    elif k==6 and not(leap(y2)):
        a[y2]=no
        no-=1
        y2-=1
    else:
        a[y2]=no
        y2-=1
    """not required part
    a[1]=1
    a[2]=1
    a[3]=1
    a[4]=1"""
for _ in range(int(input())):
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    #this is the main change, big long ass condition not needed.
    if m1>2:
        y1+=1
    if m2<2:
        y2-=1
    #the condition ends here.
    #CANT give the condition ((y2-y1+1)//2000)*505
    k1=((y2//2000)*505)-(((y1-1)//2000)*505)
    k1+=a[y2%2000]-a[(y1-1)%2000]
    print(k1)
"""
COMPARISON CODE
"""
#question is not about leap year.t happens in FEB when the first friday appears
#on 6th or 7th
"""
import math
import datetime 
import calendar
def leap(y):
    if (y%4==0 and y%100) or y%400==0:
        return 1
    return 0
def findday(y):
    return datetime.datetime(y,2,1).weekday()
a=[0]*401
y2=400
no=101
while(y2>=1):
    k=findday(y2)
    if k==5 :
        a[y2]=no
        no-=1
        y2-=1
    elif k==6 and not(leap(y2)):
        a[y2]=no
        no-=1
        y2-=1
    else:
        a[y2]=no
        y2-=1
for _ in range(int(input())):
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    k=(y2-y1+1)//400
    k*=101
    k+=a[y2%400]-a[(y1-1)%400]
    if m1>2:
        k-=1
    if m2<2:
        k-=1
    print(max(k,0))
"""
"""
COMPARISON CODE
#question is not about leap year.t happens in FEB when the first friday appears
#on 6th or 7th
import math
import datetime 
import calendar
def leap(y):
    if (y%4==0 and y%100) or y%400==0:
        return 1
    return 0
def findday(y):
    return datetime.datetime(y,2,1).weekday()
a=[0]*2001
y2=2000
no=505
while(y2>=1):
    k=findday(y2)
    if k==5 :
        a[y2]=no
        no-=1
        y2-=1
    elif k==6 and not(leap(y2)):
        a[y2]=no
        no-=1
        y2-=1
    else:
        a[y2]=no
        y2-=1
for _ in range(int(input())):
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    k=(y2-y1)//2000
    k*=505
    k+=a[(y2)%2001]-a[(y1)%2001]
    if m1>2 :
        k-=1
    if m2<2:
        k-=1
    if y2-y1<2000:
        k+=1
    print(max(k,0))
"""
        






    
 
        





