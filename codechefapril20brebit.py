mod=998244353

def modulo_multiplicative_inverse(A, M=998244353 ):
    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    return x

def extended_euclid_gcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        quotient = old_r//r 
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

def solve(a,ic,ch,p1,p2,i):
    r=4**ic[p2]
    
    if ch=="&":
        
        a[i][0]= (r * a[p1][0] + (a[p1][1] * a[p2][0]) + (a[p1][2] * (a[p2][0]+ a[p2][3])) + (a[p1][3] * (a[p2][0]+ a[p2][2])))
        a[i][1]=(a[p1][1]*a[p2][1])
        a[i][2]=((a[p1][1]*a[p2][2]) + (a[p1][2] * a[p2][2]) + (a[p1][2] * a[p2][1]))
        a[i][3]=((a[p1][1]*a[p2][3]) + (a[p1][3] * a[p2][3]) + (a[p1][3] * a[p2][1]))

    elif(ch=='|'):
    
        a[i][0]=(a[p1][0]*a[p2][0])
        a[i][1]=(r * a[p1][1] + (a[p1][0] * a[p2][1]) + (a[p1][2] * (a[p2][1]+ a[p2][3])) + (a[p1][3] * (a[p2][1] + a[p2][2])))
        a[i][2]=((a[p1][0]*a[p2][2]) + (a[p1][2] * a[p2][2]) + (a[p1][2] * a[p2][0]))
        a[i][3]=((a[p1][0]*a[p2][2]) + (a[p1][3] * a[p2][3]) + (a[p1][3] * a[p2][0]))

    elif(ch=='^'):
    
        a[i][0]=((a[p1][0]*a[p2][0]) +(a[p1][1]*a[p2][1]) + (a[p1][2]*a[p2][2]) + (a[p1][3]*a[p2][3]))
        a[i][1]=((a[p1][0]*a[p2][1]) +(a[p1][1]*a[p2][0]) + (a[p1][2]*a[p2][3]) + (a[p1][3]*a[p2][2]))
        a[i][2]=((a[p1][0]*a[p2][2]) +(a[p1][1]*a[p2][3]) + (a[p1][2]*a[p2][0]) + (a[p1][3]*a[p2][1]))
        a[i][3]=((a[p1][0]*a[p2][3]) +(a[p1][1]*a[p2][2]) + (a[p1][2]*a[p2][1]) + (a[p1][3]*a[p2][0]))
    
    ic[i]=ic[p1]+ic[p2]

for _ in range(int(input())):
    s=input()
    cnt=4**s.count('#')
    cnt=modulo_multiplicative_inverse(cnt)
    c=0
    st=[]
    sc=[]
    a=[[1 for i in range(4)] for i in range(len(s))]
    ic=[1 for i in range(len(s))]
    for k in range(len(s)):
        if s[k]=='#':
            st.append(k)
        if(s[k]=='|' or s[k]=='&' or s[k]=='^'):
            sc.append(s[k])
        if s[k]==')':
            p2=st.pop()
            p1=st.pop()
            sim=sc.pop()
            solve(a,ic,sim,p1,p2,k)
            st.append(k)
    k=st[-1]
    print(*a[k])
    for i in range(4):
        a[k][i]*=cnt
        a[k][i]%=mod
    print(*a[k])
    
    
        
    
    

"""def modulo_multiplicative_inverse(A, M=998244353 ):
    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    return x

def extended_euclid_gcd(a, b):
    s = 0 old_s = 1
    t = 1 old_t = 0
    r = b old_r = a
    while r != 0:
        quotient = old_r//r 
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

def multiply(init_soln,di,k):
    newsoln=[0,0,0,0]
    for i in range(4):
        for j in range(4):
            newsoln[i]+=init_soln[j]*di[k][i][j]
    return newsoln
"""
"""
for _ in range(int(input())):
    s=input()
    q=s.count('#')
    q1=0
    init_soln=[1,1,1,1]
    #when 0 is lhs of equation, how many times can we get 0
    di={'&':{0:[4,1,2,2],1:[0,1,0,0],2:[0,1,2,0],3:[0,1,0,2]},
        '|':{0:[1,0,0,0],1:[1,4,2,2],2:[1,0,2,0],3:[1,0,0,2]},
        '^':{0:[1,1,1,1],1:[1,1,1,1],2:[1,1,1,1],3:[1,1,1,1]}}
    operator=[]
    for i in s:
        if i==')':
            k=operator.pop()
            operator.pop()
            init_soln=multiply(init_soln,di,k)
            print(operator,init_soln)
        elif i!='#':
            operator.append(i)
        else:
            q1+=1
            q2=modulo_multiplicative_inverse(4**q1)
            for i in range(4):
                init_soln[i]*=q2
                init_soln[i]%=998244353
    print(*init_soln)
"""
"""
for _ in range(int(input())):
    s=input()
    q=s.count('#')
    q1=modulo_multiplicative_inverse(4**q)
    init_soln=[1,1,1,1]
    #when 0 is lhs of equation, how many times can we get 0
    di={'&':{0:[4,1,2,2],1:[0,1,0,0],2:[0,1,2,0],3:[0,1,0,2]},
        '|':{0:[1,0,0,0],1:[1,4,2,2],2:[1,0,2,0],3:[1,0,0,2]},
        '^':{0:[1,1,1,1],1:[1,1,1,1],2:[1,1,1,1],3:[1,1,1,1]}}
    operator=[]
    for i in s:
        if i==')':
            k=operator.pop()
            operator.pop()
            init_soln=multiply(init_soln,di,k)
            print(operator,init_soln)
        elif i!='#':
            operator.append(i)
    for i in range(4):
        init_soln[i]*=q1
        init_soln[i]%=998244353
    print(*init_soln)
"""
                    
        
