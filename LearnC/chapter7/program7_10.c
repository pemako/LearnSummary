// author <pemakoa@gmail.com>
// 内存的动态分配 使用指针来计算质数

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
	unsigned long long *pPrimes = NULL;
	unsigned long long trial = 0;
	bool found = false;
	int total = 0;
	int count = 0;
	

	printf("How many primes would you loke - you'll get at least 4? ");
	scanf("%d", &total);
	total = total < 4 ? 4 : total;

	pPrimes = (unsigned long long*)malloc(total*sizeof(unsigned long long));
	if (!pPrimes)
	{
		printf("Not enough memory. It's the end I'm afraid.\n");
		return 1;
	}

	*pPrimes = 2ULL;
	*(pPrimes + 1) = 3ULL;
	*(pPrimes + 2) = 5ULL;
	count = 3;
	trial = 5ULL;

	while(count < total) {
		trial += 2ULL;

		for (int i = 0; i < count; ++i) {
			if (!(found = (trial % *(pPrimes + i)))) break;
		}

		if(found) 
			*(pPrimes + count++) = trial;
	}

	for (int i = 0; i < total; ++i)
	{
		printf("%12llu", *(pPrimes + i));
		if (!((i + 1) % 5))
		{
			printf("\n");
		}
	}
	printf("\n");

	free(pPrimes);
	pPrimes = NULL;

	return 0;
}

