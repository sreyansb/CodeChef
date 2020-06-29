for _ in  range(int(input())):
    a,b=input().split()
    if len(a)==1 and len(b)==1:
        print(int(a)+int(b))
    elif len(a)==1 and len(b)==2:
        a0=int(a[0])
        b1=int(b[0])
        b0=int(b[1])
        print(max(b1*10+(a0+b0),a0*10+(b1+b0)))
    elif len(a)==2 and len(b)==1:
        a1=int(a[0])
        b0=int(b[0])
        a0=int(a[1])
        print(max(a1*10+(b0+a0),b0*10+(a1+a0)))
    else:
        a1=int(a[0])
        a0=int(a[1])
        b1=int(b[0])
        b0=int(b[1])
        print(max(a1*10+a0+b1*10+b0,b1*10+a0+a1*10+b0,a1*10+b1+a0*10+b0,b0*10+a0+b1*10+a1))
