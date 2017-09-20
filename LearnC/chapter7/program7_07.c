// author <pemakoa@gmail.com>

#include <stdio.h>

int main(void)
{
	char board[3][3] = {
		{'1', '2', '3'},
		{'4', '5', '6'},
		{'7', '8', '9'}
	};

	printf("address of board	: %p\n", board);
	printf("address of board[0][0]: %p\n", &board[0][0]);
	printf("value of board[0] :%p\n", board[0]);

	printf("value of board[0][0]: %c\n", board[0][0]);
	printf("value of board[0]: %c\n", *board[0]);
	printf("value of **board :%c\n", **board);

	return 0;
}

