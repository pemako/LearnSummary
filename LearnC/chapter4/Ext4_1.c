// author <pemakoa@gmail.com>
// Jun 14, 201609:18


#include <stdio.h>
#include <ctype.h>

int main(void)
{
	int number = 0;
	printf(" 请输入需要输出的乘法表的最大个数\n");
	scanf("%d", &number);

	for (int i = 1; i <= number; i++) {

		for (int j = 1; j <= i; j++){

			printf("%d * %d = %d ", j, i, i * j);
		}

		printf("\n");
	}
	
	return 0;
}