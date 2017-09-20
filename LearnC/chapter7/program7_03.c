// author <pemakoa@gmail.com>

#include <stdio.h>

int main(void)
{
	int value = 0;
	int *pvalue = &value;

	printf("Input an integer:\n");	
	scanf(" %d", pvalue);

	printf("You entered %d.\n", value);
	return 0;
}