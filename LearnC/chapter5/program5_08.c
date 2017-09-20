// author <pemakoa@gmail.com>
// Jun 15, 201621:50

#include <stdio.h>
#ifdef __STDC_NO_VLA__
	printf("Variable length arrays are not support.\n");
	exit(1);
#endif

int main(void)
{
	size_t nGrades = 0;
	printf("Enter the number of grades: ");
	scanf("%zd", &nGrades);
	int grades[nGrades];
	long sum = 0L;
	float average = 0.0f;
	printf("\nEnter the %zd grades:\n", nGrades);

	for(size_t i = 0; i < nGrades; i++) {
		printf("%2zd>\n", i + 1);
		scanf("%d", &grades[i]);
		sum += grades[i];
	}

	printf("The grades you entered are:\n");
	for(size_t i = 0; i < nGrades; ++i) {
		printf("Grade[%2zd] = %3d ", i + 1, grades[i]);

		if((i + 1) % 5 == 0) {
			printf("\n");
		}
	}

	average = (float)sum/nGrades;
	printf("\nAverage of the %zd grades entered is: %.2f\n", nGrades, average);

	return 0;
}