// author <pemakoa@gmail.com>
// Jun 14, 201609:29

#include <stdio.h>
#include <ctype.h>

int main(void)
{
	char ch = 0;
	for (int i = 0; i < 128; i++) {
		ch = (char)i;
		if (i % 2 == 0) printf("\n");
		// printf(" %4d	%c", ch, (isgraph(ch) ? ch : ' '));
		
		if (isgraph(ch)) {
			printf("	%c", ch);
		} else {
			switch(ch)
			{
				case '\n':
					printf("	newline");
					break;
				case ' ':
					printf("	space");
					break;
				case '\t':
					printf("	tab");
					break;
				case '\v':
					printf("	vertical tab");
					break;
				case '\f':
					printf("	form feed");
					break;
				default:
					printf("	");
					break;
			}
		}
	}

	printf("\n");
	return 0;
}