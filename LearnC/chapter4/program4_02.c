// author <pemakoa@gmail.com>
// Jun 13, 201623:23

#include <stdio.h>

int main(void)
{
	int sum = 0;
	for(int count = 1; count <= 100; count++) {
		sum += count;
	}	
	printf("%d \n", sum);
	return 0;
}