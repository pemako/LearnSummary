// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 23:25:54 GMT+8

// 判断从键盘上输入的一个字符串中有多少个数字、字母和标点符号
#include <stdio.h>
#include <ctype.h>
#define BUF_SIZE 100

int main(void)
{
	char buf[BUF_SIZE];
	int nLetters = 0;
	int nDigits = 0;
	int nPunct = 0;

	printf("Enter an interestring string of less than %d characters:\n", BUF_SIZE );

	if (!fgets(buf, sizeof(buf)))
	{
		printf("Error reading string\n");
		return 1;
	}
	size_t i = 0;
	while(buf[i]) {
		if(isalpha(buf[i])) ++nLetters;
		else if(isdigit(buf[i])) ++nDigits;
		else if(ispunct(buf[i])) ++nPunct;
		++i;
	}

	printf("\nYour string contained %d letters, %d digits and %d puctuntion characters.\n", 
		nLetters, nDigits, nPunct);

	return 0;
}