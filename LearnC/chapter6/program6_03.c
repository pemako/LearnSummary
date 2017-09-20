// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 21:45:35 GMT+8

// 字符串数组
#include <stdio.h>

int main(void)
{
	char str[][70]  = {
		"Computer do what you tell them to do, not what you want them to do.",
		"When you put something to memory, remember where you put it.",
		"Never test for a condition you don't know what to do with."
	};

	unsigned int count = 0;
	unsigned int strCount = sizeof(str)/sizeof(str[0]);
	printf("There are %u strings.\n", strCount);

	for (unsigned int i = 0; i < strCount; i++) {
		count = 0;
		while (str[i][count]) ++count;
		printf("The string:\n 	\"%s\"\n contains %u characters.\n ", str[i], count);
	}
	return 0;
}