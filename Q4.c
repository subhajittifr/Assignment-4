
#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main()
{
	int n,i;
	n=10000;
	double y[n],x;

	FILE *fp;
	fp=fopen("Q4.txt","w");

	for(i=0;i<n;i++)
	{
		x=rand()/((double)RAND_MAX+1);
		y[i]=-0.5*log(1-x);
		fprintf(fp,"%0.6f\n",y[i]);
	}

	fclose(fp);
	/* The plotting has been done on pyplot, the .py file is attached */
}
