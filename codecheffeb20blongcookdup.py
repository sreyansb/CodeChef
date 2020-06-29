#question is not about leap year.t happens in FEB when the first friday appears
#on 6th or 7th
import datetime 
import calendar
def leap(y):
    if (y%4==0 and y%100) or y%400==0:
        return 1
    return 0
def findday(y):
    return datetime.datetime(y,2,1).weekday()
for _ in range(int(input())):
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    z=y2
    no=0
    la=0
    fy=0
    while(y2>=y1):
        k=findday(y2)
        if k==5 :
            if fy==0:
                fy=y2
            no+=1
            la=y2
            y2-=5
        elif k==6 and not(leap(y2)):
            if fy==0:
                fy=y2
            no+=1
            la=y2
            y2-=1
        else:
            y2-=1
    if m2<2 and fy==z:
        no-=1
    if m1>2 and la==y1 :
        no-=1
    print(max(0,no))
    

  

  
""" 
date = '03 02 2019'
print(findDay(date))
"""
        
        


