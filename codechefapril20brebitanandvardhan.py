def modinv(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
  
def and_operation(p00,p11,p01,p10):
    temp00=(p00*4)+(p11*1)+(p01*2)+(p10*2)
    temp11=(p00*0)+(p11*1)+(p01*0)+(p10*0)
    temp01=(p00*0)+(p11*1)+(p01*2)+(p10*0)
    temp10=(p00*0)+(p11*1)+(p01*0)+(p10*2)
    return(temp00,temp11,temp01,temp10)
def or_operation(p00,p11,p01,p10):
    temp00=(p00*1)
    temp11=(p00*1)+(p11*4)+(p01*2)+(p10*2)
    temp01=(p00*1)+(p11*0)+(p01*2)+(p10*0)
    temp10=(p00*1)+(p11*0)+(p01*0)+(p10*2)
    return(temp00,temp11,temp01,temp10)    
def xor_operation(p00,p11,p01,p10):
    temp00=(p00*1)+(p11*1)+(p01*1)+(p10*1)
    temp11=(p00*1)+(p11*1)+(p01*1)+(p10*1)
    temp01=(p00*1)+(p11*1)+(p01*1)+(p10*1)
    temp10=(p00*1)+(p11*1)+(p01*1)+(p10*1)
    return(temp00,temp11,temp01,temp10)

def Infix(expr):
    p00=1
    p11=1
    p01=1
    p10=1
    count_num=0
    count_num=expr.count("#")
    expr = list(expr)
    stack = list()
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if c=="#":
            num += c
        else:
            if num != "":
                stack.append(num)
                num = ""
            if c in "&|^":
                stack.append(c)
            elif c == ")":
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                if op == "&":
                    (p00,p11,p01,p10)=and_operation(p00,p11,p01,p10)   
                    stack.append("#")
                elif op == "|":
                    (p00,p11,p01,p10)=or_operation(p00,p11,p01,p10) 
                    stack.append("#")
                elif op == "^":
                    (p00,p11,p01,p10)=xor_operation(p00,p11,p01,p10)   
                    stack.append("#")               
    base=pow(4,count_num)
    q=modinv(base,998244353)
    print(p00,p11,p01,p10)
    print((p00*q)%998244353,end=" ")
    print((p11*q)%998244353,end=" ")
    print((p01*q)%998244353,end=" ")
    print((p10*q)%998244353)


t=int(input())
for _ in range(t):
    string=input()  
    Infix(string)
