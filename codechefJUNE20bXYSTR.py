for _ in range(int(input())):
    s=input()
    n=len(s)
    i=0
    number=0
    while(i+1<n):
        if (s[i]=='x' and s[i+1]=='y') or (s[i]=='y' and s[i+1]=='x'):
            number+=1
            i+=2
        else:
            i+=1
    print(number)
