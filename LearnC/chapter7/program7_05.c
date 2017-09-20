// author <pemakoa@gmail.com>
// 将一个整数值加到指针上的结果

#include <stdio.h>
#include <string.h>

int main(void)
{
	char multiple[] = "a string";
	char *p = multiple;

	for (int i = 0; i < strlen(multiple); ++i)
	{
		printf("multiple[%d] = %c * (p + %d) = %c &multiple[%d] = %p p+%d = %p\n",
		i, multiple[i], i, *(p+i),i, &multiple[i], i, p+i);
	}	
	return 0;
}

