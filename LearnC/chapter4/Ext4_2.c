// author <pemakoa@gmail.com>
// Jun 14, 201609:29

#include <stdio.h>
#include <ctype.h>

int main(void)
{
	char ch = 0;
	for (int i = 0; i < 128; i++) {
		ch = (char)i;
		if (i % 8 == 0) printf("\n");
		printf(" %4d	%c", ch, (isgraph(ch) ? ch : ' '));
	}

	printf("\n");
	return 0;
}