// author <pemakoa@gmail.com>
// Jun 13, 201621:11
// 这个程序判断输入的数据是偶数还是奇数

#include <stdio.h>
#include <limits.h>

int main(void)
{
	long test = 0L;

	printf("Enter an integer less than %ld:", LONG_MAX);
	scanf("%ld", &test);

	if (test % 2L == 0L) {
		printf("The number %ld is even\n", test);

		// Now check whether half the number is also even
		if ((test/2L) % 2L == 0L){
			printf("\nHalf of %ld is also even", test);
			printf("\nThat's interestring isn't it?\n");
		}
	}
	else{
		printf("The number %ld is odd\n", test);
	}
	return 0;
}