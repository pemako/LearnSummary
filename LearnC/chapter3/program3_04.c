// author <pemakoa@gmail.com>
// Jun 13, 201621:25
// 将输入的大写字母转换为小写字母

#include <stdio.h>

int main(void)
{
	char letter = 0;

	printf("Enter an uppercase letter:\n");
	scanf("%c", &letter);

	if ((letter >= 'A') && (letter <= 'Z'))
	{
		letter = letter - 'A' + 'a';
		printf("You entered an uppercase %c\n", letter);
	}
	else {
		printf("Try using the shift key ! I want a capital letter .\n");
	}
	return 0;
}