// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 23:58:01 GMT+8

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define TEXT_LEN 10000
#define BUF_SIZE 100
#define MAX_WORDS 500
#define WORD_LEN 12

int main(void)
{
	char delimitersp[] = " \n\".,;:!?)(";
	char text[TEXT_LEN] = "";
	char buf[BUF_SIZE];
	char words[MAX_WORDS][WORD_LEN];
	int nword[MAX_WORDS] = {0};
	int word_count = 0;

	printf("Enter text on an arbitrary number of lines.\n");
	printf("\nEnter an empty line to end input:\n");

	while(true) {
		fgets(buf, BUF_SIZE, stdin);
		if(buf[0] == '\n') break;

		if(strlen(strcat(text,buf)) > TEXT_LEN)  {
			printf("Maximus capacity for text exceeded. \n");
			return 1;
		}
	}

	return 0;
}