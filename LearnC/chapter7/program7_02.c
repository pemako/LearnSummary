// author <pemakoa@gmail.com>

#include <stdio.h>

int main(void)
{
	long num1 = 0L;
	long num2 = 0L;
	long *pnum = NULL;

	pnum = &num1;
	*pnum = 2L;
	++num2;
	num2 += *pnum;

	pnum = &num2;
	++*pnum;

	printf("num1 = %ld num2 = %ld *pnum = %ld *pnum + num1 = %ld\n",
		num1, num2, *pnum, *pnum + num2);	
	return 0;
}