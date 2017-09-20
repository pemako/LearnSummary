// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 21:53:49 GMT+8

// 检查对 C11的支持
// 要使用 string.h 中的可选函数，必须在 string.h的 include 语句之前，在
// 源文件中定义 __STDC_WANT_LIB_EXT1__符号，来表示值1
/*
#include <stdio.h>

int main(void)
{

#if defined __STDC_LIB_EXT1__
	printf("Opthional functions are defined.\n");
#else
	printf("Opthional functions are not defined\n");
#endif
	return 0;
}
*/

// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 21:57:50 GMT+8

#define __STDC_WANT_LIB_EXT1__ 1
#include <string.h>
#include <stdio.h>
 
int main(void)
{
    const char str[] = "How many characters does this string contain?";
 
    printf("without null character: %zu\n", strlen(str));
    printf("with null character:    %zu\n", sizeof str);
 
#ifdef __STDC_LIB_EXT1__
    printf("without null character: %zu\n", strnlen_s(str, sizeof str));
#endif
}