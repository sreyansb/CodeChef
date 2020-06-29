#include<stdio.h>
#include<stdlib.h>
int block_sz=0;
int N=100005;
int *parent=calloc(N,sizeof(int));
int *depth=calloc(N,sizeof(int));
int *jump_parent=calloc(N,sizeof(int));
long long int mod=1000000000+7;

