// author <pemakoa@gmail.com>
// Jun 15, 201621:40

#include <stdio.h>

int main(void)
{
	int numbers[3][4] = {
		{10, 20, 30, 40},
		{15, 25, 35, 45},
		{47, 48, 49, 50}
	};

	int sum = 0;

	for(int i = 0; i < sizeof(numbers)/sizeof(numbers[0]); ++i){
		for(int j = 0; j < sizeof(numbers[0])/sizeof(numbers[0][0]); ++j) {
			sum += numbers[i][j];
		}
	}	

	printf("%d\n", sum);
	return 0;
}