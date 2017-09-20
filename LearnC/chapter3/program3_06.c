// author <pemakoa@gmail.com>
// Jun 13, 201622:09

#include <stdio.h>

enum week {
	sunday,
	monday,
	tuesday,
	wednesday,
	thursday,
	friday,
	saturday
};

int main(void)
{
	enum week today;
	today = wednesday;
	printf("%d day\n", today + 1);

	return 0;
}