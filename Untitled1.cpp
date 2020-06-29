#include <bits/stdc++.h>
using namespace std;
int main()
{int t;

    cin>>t;
    while(t--)
    {int m,n;
    cin>>m>>n;
    int total=m*n;
    int a[m][n];
    for (int i=0;i<m;i++)
    {for(int j=0;j<n;j++)
    cin>>a[i][j];}
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
    cout<<total<<endl;
    }
return 0;
    }

