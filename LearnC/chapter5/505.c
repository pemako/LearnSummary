#include<stdio.h>
#ifdef __STDC_NO_VLA__
    printf("Variable length arrays are not supported.\n");
#endif

int main(void)
{
	int sum = 0;
	int numbers[2][3][4] = {
		{
			{10, 20, 30, 40 },
			{15, 25, 35, 45 },
			{47, 48, 49, 50}
		},
		{
			{10, 20, 30, 40 },
			{15, 25, 35, 45 },
			{47, 48, 49, 50}
		}
	};

	for (int i = 0; i < sizeof(numbers) / sizeof(numbers[0]); ++i)
	{
		for (int j = 0; j < sizeof(numbers[0])/sizeof(numbers[0][0]); ++j)
		{
			for (int k = 0; k < sizeof(numbers[0][0])/sizeof(numbers[0][0][0]); ++k)
			{
				sum += numbers[i][j][k];
			}
		}
	}

	printf("%d\n", sum);
	return 0;
}