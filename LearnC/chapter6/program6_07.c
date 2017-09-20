// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 22:50:34 GMT+8

#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[] = "Peterpiper picked a peck of pickled pepper.";
	char ch = 'p';
	char *pGot_char = str;
	int count = 0;
	while(pGot_char =  strchr(pGot_char, ch)) {
		// pGot_char = strchr(pGot_char, ch);
		++count;
		++pGot_char;
	}
	printf("The character '%c' was found %d times in the following string:\n\"%s\"\n", ch, count, str);
	return 0;
}