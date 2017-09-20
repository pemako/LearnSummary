// author <pemakoa@gmail.com>
// Jun 13, 201621:41

#include <stdio.h>
#include <ctype.h>

int main(void)
{
	char letter = 0;
	printf("Enter an uppercase letter:\n");
	scanf("%c", &letter);

	if (isalpha(letter) && isupper(letter))
	{
		printf("You entered an uppercase letter.\n");
	} else {
		printf("You did not enter an uppercase letter.\n");
	}
	
	return 0;
}