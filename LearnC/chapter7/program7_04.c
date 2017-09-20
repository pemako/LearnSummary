// author <pemakoa@gmail.com>
// 数组名称本身引用了一个地址

#include <stdio.h>

int main(void)
{
	char multiple[] = "My string";

	char *p = &multiple[0];
	printf("The address of the first array element: %p\n", p);

	p = multiple;
	printf("The address obtained from the array name: %p\n", multiple);
	return 0;
}

