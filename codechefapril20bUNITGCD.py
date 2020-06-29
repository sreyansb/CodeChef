for _ in range(int(input())):
    n=int(input())
    listfinal=[]
    lenoffinal=0
    initialist=list(range(1,min(4,n+1)))
    initialist=[len(initialist)]+initialist
    lenoffinal+=1
    listfinal.append(initialist)
    for i in range(4,n+1,2):
        initialist=list(range(i,min(i+2,n+1)))
        initialist=[len(initialist)]+initialist
        listfinal.append(initialist)
        lenoffinal+=1
    print(lenoffinal)
    for i in listfinal:
        print (*i)

        
    
