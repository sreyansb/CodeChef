arr=[1,2,3,4]
for k in range(0,35):
    summ=0
    xor=0
    for i in arr:
        summ+=i^k
        xor^=i
    print(k,summ,xor,bin(summ)[2:])
