#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{   int 
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int m,n;
        scanf("%d %d",&n,&m);
        int *xneg=calloc(100005,sizeof(int));
        int *xpos=calloc(100005,sizeof(int));
        int *yneg=calloc(100005,sizeof(int));
        int *ypos=calloc(100005,sizeof(int));
        int *dix=calloc(100005,(sizeof(int)));
        int *diy=calloc(100005,(sizeof(int)));
        int xp=0;int yp=0;int xn=0;int yn=0;
        int xz=0;
        int yz=0;
        for (int i=0;i<n;i++)
        {int j;scanf("%d",&j);
        if (j<0)
            {xneg[-j]=1;xn=xn<-j?-j:xn;}
        else if (j>0)
            {xpos[j]=1;xp=j;}
        else
            xz=1;
        dix[abs(j)]+=1;
        }
        for (int i=0;i<m;i++)
        {int j;scanf("%d",&j);
        if (j<0)
            {yneg[-j]=1;yn=yn<-j?-j:yn;}
        else if (j>0)
            {ypos[j]=1;yp=j;}
        else
            yz=1;
        diy[abs(j)]+=1;     
        }
        int no=0;
        if (xz)
            no=(n-1)*m;
        if (yz)
            no=(m-1)*n;
        if (xz && yz)
            no=(m-1)*(n-1);
        for(int i=1;i<=xp;++i)
        {	int j=i;
			while()
        	while(diy[i*j*-1]])
            {no+=diy[i*j*-1];
            j*=j;}
        }
        for(int i=0;i<=yp;++i)
        {
            for(int j=0;j<yn;++j)
            {double height = sqrt(ypos[i]*yneg[j]*-1);
            if (height==(int)(height))
                no+=dix[(int)(height)];
            }
        }
        printf("%d\n",no);
    }
    return 0;
}
