// author <pemakoa@gmail.com>
// Jun 13, 201622:39
// 按位于操作

#include <stdio.h>

int main(void)
{
	unsigned int original = 0xABC;
	unsigned int result = 0;
	unsigned int mask = 0xF;

	printf("\n original = %X\n", original);

	// Insert firset digit in result
	result |= original & mask;

	printf("%X\n", result);
	return 0;
}