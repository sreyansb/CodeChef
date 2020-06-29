#include <stdio.h>
int main()
{int t;
int a[100005][100005];
    scanf("%d",&t);
    while(t--)
    {int m,n;
    scanf("%d %d",&m,&n);
    int total=m*n;
    for (int i=0;i<m;i++)
    {for(int j=0;j<n;j++)
    scanf("%d",&a[i][j]);}
    for(int i=1;i<m;i++)
    {
    for(int j=1;j<n;j++)
    {int i1=1;
	while(i>=i1 && i+i1<m && j>=i1 && j+i1<n)
    {if (a[i][j-i1]==a[i][j+i1] && a[i-i1][j]==a[i+i1][j])
    {total+=1;i1+=1;}
    else
    break;}}
    }
    printf("%d\n",total);
    }
return 0;
    }

