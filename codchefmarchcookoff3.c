#include<stdio.h>
int calc(int a, int b)
{
	int no=1;
	while(a>0 && b>0)
	{
		if (a%2)
		{
			if (b%2)
				no<<=1;
			else
			{
				no=0;
				break;
			}
		}
		a=a>>1;
		b=b>>1;
	}
	return no;
}

int main()
{	int t;
	scanf("%d",&t);
	while(t--)
	{
	int n;
	scanf("%d",&n);
	int a[n];
	long int nof=1;
	for (int i=0;i<n;++i)
		{scanf("%d",a+i);}
	long int nofi;
	long int k=1000000000+7;
	for(int i=1;i<n;++i)
	{
		nofi=calc(a[i-1],a[i]);
		nof=((nof%k)*(nofi%k))%k;
	}
	printf("%ld\n",nof);}
}
