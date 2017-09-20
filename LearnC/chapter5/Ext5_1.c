// author <pemakoa@gmail.com>
// Wednesday, June 15, 2016 22:42:46 GMT+8

// 从键盘上读入5个 double 类型的值，将他们存储到一个数组中。计算每个值的倒数(值 x的倒数为 1.0/x)
// 将结果存储到另一个数组中。输入这写倒数，并计算和输出倒数的总和


#include <stdio.h>

int main(void)
{
	const int nValues = 5;
	double data[nValues];
	double reciprocals[nValues];
	double sum = 0.0;

	printf("Enter five values separated by spaces: \n");
	for (int i = 0; i < nValues; i++)
		scanf("%lf", &data[i]);

	printf("You entered the values:\n");
	for(int i = 0; i < nValues; i++)
		printf("%15.2lf", data[i]);
	printf("\n");

	printf("\nThe value of the reciprocals are: \n");
	for (int i = 0; i < nValues; i++){
		reciprocals[i] = 1.0/data[i];
		printf("%15.2lf", reciprocals[i]);
	}
	printf("\n\n");

	for(int i = 0; i < nValues; i++) {
		sum += reciprocals[i];
		if(i > 0) printf(" + ");
		printf("1/%.2lf", data[i]);
	}

	printf(" = %lf\n", sum);

	return 0;
}