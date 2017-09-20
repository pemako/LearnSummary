// author <pemakoa@gmail.com>
// Jun 15, 201620:56

#include <stdio.h>

int main(void)
{
	double value[5] = {1.5, 2.5, 3.5, 4.5, 5.5};
	size_t element_count = sizeof(value)/sizeof(value[0]);
	double sum = 0.0;

	// printf("%zu",element_count);	

	for (unsigned int i = 0; i < sizeof(value)/sizeof(value[0]); ++i)
		printf("%f\n",value[i]); 
		sum += value[i];
		printf("%f\n", sum);
		// printf("%f\n", value[i]);
		// sum += value[i];

	printf("%.2f\n", sum);

	printf("%lu\n", sizeof(value));
	printf("%lu\n", sizeof(value[0]));

	return 0;
}