// author <pemakoa@gmail.com>
// Incrementing a pointer to an array of integers

#include <stdio.h>

int main(void)
{
	long multiple[] = {15L, 25L,35, 45L};
	long *p = multiple;

	for (int i = 0; i < sizeof(multiple)/sizeof(multiple[0]); ++i)
	{
		printf("address p + %d (&multiple[%d]) : %llu * (p + %d) value: %d\n", 
			i,i, (unsigned long long)(p + i), i, *(p+i));
	}
	return 0;
}

