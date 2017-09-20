// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 21:26:22 GMT+8

// 这个程序会输出 The character 因为 printf 函数遇到第一个空字符\0时，就会停止输出
// 即使在字符串的末尾还有另一个\0,也用不会执行。
// 注意： 在声明存储字符串的数组时，其大小至少要比所有存储的字符数多1，因为编译器会自
// 动在字符串常量的尾部添加\0

#include <stdio.h>

int main(void)
{
	printf("The character \0 is userd to terminate a string. \n");
	return 0;
}