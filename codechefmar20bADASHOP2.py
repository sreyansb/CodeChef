l=["1 1",
   "2 2","3 1","1 3","2 2",
   "3 3","4 2","5 1","1 5","2 4","3 3",
   "4 4","5 3","6 2","7 1","1 7","2 6","3 5","4 4",
   "5 5","6 4","7 3","8 2","2 8","3 7","4 6","5 5",
   "6 6","7 5","8 4","4 8","5 7","6 6",
   "7 7","8 6","6 8","7 7",
   "8 8"]

for _ in range(int(input())):
    k=input()
    print(len(l)-1)
    j=l[l.index(k)+1:]
    i=l[:l.index(k)]
    print(*j,sep="\n")
    print(*i,sep="\n")
    
