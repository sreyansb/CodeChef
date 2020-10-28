"""
zzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaaa
zzzzzzzzzzzzzzaaaaaaaa
"""
#1st attempt
for _ in range(int(input())):
    s=input()
    p=input()
    counts=[0]*26
    for i in s:
        counts[ord(i)-97]+=1
    tail=-1
    for i in p:
        counts[ord(i)-97]-=1
        if i!=p[0] and tail==-1:
            tail=ord(i)-97
    suffix=""
    prefix=""
    head=ord(p[0])-97
    for i in range(26):
        if i<head:
            prefix+=chr(i+97)*counts[i]
        elif i>head:
            suffix+=chr(i+97)*counts[i]
        else:
            if tail<head:
                suffix+=chr(i+97)*counts[i]
            else:
                prefix+=chr(i+97)*counts[i]
    print(prefix+p+suffix)


#2nd attempt
"""
for _ in range(int(input())):
    s=input()
    p=input()
    counts=[0]*26
    for i in s:
        counts[ord(i)-97]+=1
    x=p[0]
    z=-1
    for i in p:
        counts[ord(i)-97]-=1
        if z==-1 and i!=x:
            z=ord(i)-97
    x=ord(p[0])-97
    ans=""
    for i in range(26):
        if i==x:
            if z<x:
                ans+=p
                ans+=counts[i]*chr(i+97)
            else:
                ans+=counts[i]*chr(i+97)
                ans+=p
        else:
            ans+=counts[i]*chr(i+97)
    print(ans)
"""
