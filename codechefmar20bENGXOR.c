#include<stdio.h>
int parity(int x)
{
    int y;
    y=x^(x>>1);
    y=y^(y>>2);
    y=y^(y>>4);
    y=y^(y>>8);
    y=y^(y>>16);
    return (y&1);
}
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;int q;
        scanf("%d %d",&n,&q);
        int nofoddparity=0;
        for (int i=0;i<n;++i)
        {
            int k;
            scanf("%d",&k);
            nofoddparity+=parity(k);
            
        }
        int nofevenparity=n-nofoddparity;
        for(int i=0;i<q;++i)
        {
            int k;
            scanf("%d",&k);
            int parityofk=parity(k);
            if (parityofk)
                printf("%d %d\n",nofoddparity,nofevenparity);
            else
            {
                printf("%d %d\n",nofevenparity,nofoddparity);
            }
            
        }
    }
    return 0;
}
