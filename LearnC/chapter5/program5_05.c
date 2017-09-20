// author <pemakoa@gmail.com>
// Jun 15, 201620:38
// 输出变量的地址

#include <stdio.h>

int main(void)
{
	long a = 1L;
	long b = 2L;
	long c = 3L;

	double d = 4.0;
	double e = 5.0;
	double f = 6.0;

	printf("A variable of type long occupies %lu bytes.\n", sizeof(long));
	printf("A 变量的地址是 %p, B 变量的地址 %p", &a, &b);
	printf("C 变量的地址是 %p, D 变量的地址 %p", &c, &d);
	printf("E 变量的地址是 %p, F 变量的地址 %p", &e, &f);


	return 0;
}