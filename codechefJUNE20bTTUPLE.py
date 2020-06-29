def checktrue(div,diff,val,p,f):
    if((p[1]-p[0])!=0 and (f[1]-f[0])%(p[1]-p[0])==0):
        x=(f[1]-f[0])//(p[1]-p[0])
        y=f[0]-p[0]*x
        if(f[2]-p[2]*x==y):
            return 1
    if((f[1]-f[0])!=0 and (f[0]*p[1]-f[1]*p[0])%(f[1]-f[0])==0):
        x=int((f[0]*p[1]-f[1]*p[0])/(f[1]-f[0]))
        if(p[0]+x==0):
            return 0
        y=int(f[0]/(p[0]+x))
        if(p[2]+x!=0 and f[2]%(p[2]+x)==0 and f[2]/(p[2]+x)==y):
            return 1
    return 0

def check(a,b,c,div,val,p,f,diff):
    if(val[b] and val[c] and p[a]*div[b]*div[c]==f[a]):
        return 1
        
    elif(p[a]+diff[b]+diff[c]==f[a]):
        return 1
        
    elif(val[b] and p[a]*div[b]+diff[c]==f[a]):
        return 1
        
    elif(val[b] and (p[a]+diff[c])*div[b]==f[a]):
        return 1
        
    elif(val[c] and p[a]*div[c]+diff[b]==f[a]):
        return 1
        
    elif(val[c] and (p[a]+diff[b])*div[c]==f[a]):
        return 1
        
    else:
        return 0

def check2(a,div,diff,p,f):
    ind=[]
    for i in range(3):
        if(i!=a):
            ind.append(i)
    if(p[ind[1]]-p[ind[0]]!=0 and (f[ind[1]]-f[ind[0]])%(p[ind[1]]-p[ind[0]])==0):
        i=int((f[ind[1]]-f[ind[0]])/(p[ind[1]]-p[ind[0]]))
        if(f[ind[0]]-i*p[ind[0]]==diff[a]):
            return 1
    return 0

def check1(a,mul,add,val,p,fin):
    ind=[]
    for i in range(3):
        if(i!=a):
            ind.append(i)
    if(add[ind[0]]-add[a]==add[ind[1]]):
        return 1
        
    elif(add[ind[1]]-add[a]==add[ind[0]]):
        return 1
        
    elif(val[a] and fin[ind[0]]-p[ind[0]]*mul[a]==fin[ind[1]]-p[ind[1]]):
        return 1
        
    elif(val[a] and fin[ind[1]]-p[ind[1]]*mul[a]==fin[ind[0]]-p[ind[0]]):
        return 1
        
    elif(val[a] and fin[ind[0]]-p[ind[0]]*mul[a]==fin[ind[1]]-p[ind[1]]*mul[a]):
        return 1
        
    elif((p[ind[0]]+add[a])!=0 and val[ind[1]] and fin[ind[0]]%(p[ind[0]]+add[a])==0 and fin[ind[0]]/(p[ind[0]]+add[a])==mul[ind[1]]):
        return 1
        
    elif((p[ind[1]]+add[a])!=0 and val[ind[0]] and fin[ind[1]]%(p[ind[1]]+add[a])==0 and fin[ind[1]]/(p[ind[1]]+add[a])==mul[ind[0]]):
        return 1
        
    else:
        if(p[ind[1]]+add[a]!=0 and p[ind[0]]+add[a]!=0):
            x=p[ind[0]]+add[a]
            y=p[ind[1]]+add[a]
            if(fin[ind[0]]%x==0 and fin[ind[1]]%y==0 and int(fin[ind[0]]/x)==int(fin[ind[1]]/y)):
                return 1
        if(val[a] and p[ind[1]]*mul[a]!=0 and p[ind[0]]*mul[a]!=0):
            x=p[ind[0]]*mul[a]
            y=p[ind[1]]*mul[a]
            if(fin[ind[0]]%x==0 and fin[ind[1]]%y==0 and int(fin[ind[0]]/x)==int(fin[ind[1]]/y)):
                return 1
        return 0


for _ in range(int(input())):
    p=list(map(int,input().split()))
    f=list(map(int,input().split()))
    nosteps=0
    if p==f:
        print(0)
    else:
        diff=[f[i]-p[i] for i in range(3)]
        div=[f[i]/p[i] if p[i]!=0 and f[i]%p[i]==0 else 0 for i in range(3)]
        val=[1 if p[i]!=0 and f[i]%p[i]==0 else 0 for i in range(3)]
        count=0
        for i in range(3):
            if f[i]==p[i]:
                count+=1
        eq=list(set([i if p[i]!=f[i] else 0 for i in range(3)])-{0})
        if count==2:
            print(1)
        elif count==1:
            if((diff[eq[0]]==diff[eq[1]]) or ((val[eq[0]]==1 and val[eq[1]]==1 and div[eq[0]]==div[eq[1]]))):
                print(1)
            else:
                print(2)
        else:
            if((diff[0]==diff[1] and diff[1]==diff[2]) or (val[0] and val[1] and val[2] and div[0]==div[1] and div[2]==div[1])):
                print(1)
            elif((diff[0]==diff[1]) or (val[0] and val[1] and div[0]==div[1])):
                print(2)
            elif((diff[1]==diff[2]) or (val[1] and val[2] and div[1]==div[2])):
                print(2)
            elif((diff[0]==diff[2]) or (val[0] and val[2] and div[0]==div[2])):
                print(2)
            elif checktrue(div,diff,val,p,f):
                print(2)
            elif check2(0,div,diff,p,f):
                print(2)
            elif check2(1,div,diff,p,f):
                print(2)
            elif check2(2,div,diff,p,f):
                print(2)
            elif check1(0,div,diff,val,p,f):
                print(2)
            elif check1(1,div,diff,val,p,f):
                print(2)
            elif check1(2,div,diff,val,p,f):
                print(2)
            elif check(0,1,2,div,val,p,f,diff):
                print(2)
            elif check(1,0,2,div,val,p,f,diff):
                print(2)
            elif check(2,0,1,div,val,p,f,diff):
                print(2)
            else:
                print(3) 


"""
def check1(a,mul,add,val,ini,fin):
    ind=[]
    for i in range(3):
        if(i!=a):
            ind.append(i)
    if(add[ind[0]]-add[a]==add[ind[1]]):
        return 1
        
    elif(add[ind[1]]-add[a]==add[ind[0]]):
        return 1
        
    elif(val[a] and fin[ind[0]]-ini[ind[0]]*mul[a]==fin[ind[1]]-ini[ind[1]]):
        return 1
        
    elif(val[a] and fin[ind[1]]-ini[ind[1]]*mul[a]==fin[ind[0]]-ini[ind[0]]):
        return 1
        
    elif(val[a] and fin[ind[0]]-ini[ind[0]]*mul[a]==fin[ind[1]]-ini[ind[1]]*mul[a]):
        return 1
        
    elif((ini[ind[0]]+add[a])!=0 and val[ind[1]] and fin[ind[0]]%(ini[ind[0]]+add[a])==0 and fin[ind[0]]/(ini[ind[0]]+add[a])==mul[ind[1]]):
        return 1
        
    elif((ini[ind[1]]+add[a])!=0 and val[ind[0]] and fin[ind[1]]%(ini[ind[1]]+add[a])==0 and fin[ind[1]]/(ini[ind[1]]+add[a])==mul[ind[0]]):
        return 1
        
    else:
        if(ini[ind[1]]+add[a]!=0 and ini[ind[0]]+add[a]!=0):
            x=ini[ind[0]]+add[a]
            y=ini[ind[1]]+add[a]
            if(fin[ind[0]]%x==0 and fin[ind[1]]%y==0 and int(fin[ind[0]]/x)==int(fin[ind[1]]/y)):
                return 1
        if(val[a] and ini[ind[1]]*mul[a]!=0 and ini[ind[0]]*mul[a]!=0):
            x=ini[ind[0]]*mul[a]
            y=ini[ind[1]]*mul[a]
            if(fin[ind[0]]%x==0 and fin[ind[1]]%y==0 and int(fin[ind[0]]/x)==int(fin[ind[1]]/y)):
                return 1
        return 0
        
            
        
def check(a,b,c,mul,val,ini,fin,add):
    if(val[b] and val[c] and ini[a]*mul[b]*mul[c]==fin[a]):
        return 1
        
    elif(ini[a]+add[b]+add[c]==fin[a]):
        return 1
        
    elif(val[b] and ini[a]*mul[b]+add[c]==fin[a]):
        return 1
        
    elif(val[b] and (ini[a]+add[c])*mul[b]==fin[a]):
        return 1
        
    elif(val[c] and ini[a]*mul[c]+add[b]==fin[a]):
        return 1
        
    elif(val[c] and (ini[a]+add[b])*mul[c]==fin[a]):
        return 1
        
    else:
        return 0
        
def check2(a,mul,add,val,ini,fin):
    ind=[]
    for i in range(3):
        if(i!=a):
            ind.append(i)
    if(ini[ind[1]]-ini[ind[0]]!=0 and (fin[ind[1]]-fin[ind[0]])%(ini[ind[1]]-ini[ind[0]])==0):
        i=int((fin[ind[1]]-fin[ind[0]])/(ini[ind[1]]-ini[ind[0]]))
        if(fin[ind[0]]-i*ini[ind[0]]==add[a]):
            return 1
    return 0
    
def checktrue(mul,add,val,ini,fin):
    if((ini[1]-ini[0])!=0 and (fin[1]-fin[0])%(ini[1]-ini[0])==0):
        x=int((fin[1]-fin[0])/(ini[1]-ini[0]))
        y=fin[0]-ini[0]*x
        if(fin[2]-ini[2]*x==y):
            return 1
    if((fin[1]-fin[0])!=0 and (fin[0]*ini[1]-fin[1]*ini[0])%(fin[1]-fin[0])==0):
        x=int((fin[0]*ini[1]-fin[1]*ini[0])/(fin[1]-fin[0]))
        if(ini[0]+x==0):
            return 0
        y=int(fin[0]/(ini[0]+x))
        if(ini[2]+x!=0 and fin[2]%(ini[2]+x)==0 and fin[2]/(ini[2]+x)==y):
            return 1
    return 0
        
    
    

for _ in range(int(input())):
    ini=list(map(int,input().split()))
    fin=list(map(int,input().split()))
    add=[]
    mul=[0,0,0]
    val=[0,0,0]
    eq=[]
    for i in range(3):
        add.append(fin[i]-ini[i])
    for i in range(3):
        if(ini[i]!=0 and fin[i]%ini[i]==0):
            val[i]=1 
            mul[i]=int(fin[i]/ini[i])
    count=0
    for i in range(3):
        if(fin[i]==ini[i]):
            count+=1
        else:
            eq.append(i)
    if(count==3):
        print(0)
    elif(count==2):
        print(1)
    elif(count==1):
        if((add[eq[0]]==add[eq[1]]) or ((val[eq[0]]==1 and val[eq[1]]==1 and mul[eq[0]]==mul[eq[1]]))):
            print(1)
        else:
            print(2)
    else:
        if((add[0]==add[1] and add[1]==add[2]) or (val[0] and val[1] and val[2] and mul[0]==mul[1] and mul[2]==mul[1])):
            print(1)
        elif((add[0]==add[1]) or (val[0] and val[1] and mul[0]==mul[1])):
            print(2)
        elif((add[1]==add[2]) or (val[1] and val[2] and mul[1]==mul[2])):
            print(2)
        elif((add[0]==add[2]) or (val[0] and val[2] and mul[0]==mul[2])):
            print(2)
        elif(checktrue(mul,add,val,ini,fin)):
            print(2)
        elif(check2(0,mul,add,val,ini,fin)):
            print(2)
        elif(check2(1,mul,add,val,ini,fin)):
            print(2)
        elif(check2(2,mul,add,val,ini,fin)):
            print(2)
        elif(check1(0,mul,add,val,ini,fin)):
            print(2)
        elif(check1(1,mul,add,val,ini,fin)):
            print(2)
        elif(check1(2,mul,add,val,ini,fin)):
            print(2)
        elif(check(0,1,2,mul,val,ini,fin,add)):
            print(2)
        elif(check(1,0,2,mul,val,ini,fin,add)):
            print(2)
        elif(check(2,0,1,mul,val,ini,fin,add)):
            print(2)
        else:
            print(3)
"""

            

                    
                    
                
            
        
        
    
