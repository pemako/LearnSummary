// author <pemakoa@gmail.com>
// Jun 13, 201623:47
// 伪随机数生成

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	int number = 0;
	int limit = 20;
	srand(time(NULL));
	number = 1 + rand() % 20;

	printf("%d\n", number);
	return 0;
}