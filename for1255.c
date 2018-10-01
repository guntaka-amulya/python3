#include<stdio.h>
int main()
{
int n;
long int f=1;
printf("enter a number\n");
scanf("%d",&n);
for(;n>0;n--)
{
f*=n;
printf("\n factorial is %1d",f);
return 0;
}
}
