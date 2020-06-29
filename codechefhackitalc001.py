for i in range(int(input())):
    a=list(input())
    l=len(a)
    no=list(range(1,l+2))
    for i in range(l):
        if a[i]=="-":
            temp=no[i];
            no[i]=no[i+1]
            no[i+1]=temp
    for i in no:
        print(i,end=" ")
    print()
