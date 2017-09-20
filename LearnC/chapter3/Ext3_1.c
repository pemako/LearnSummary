// author <pemakoa@gmail.com>
// Jun 13, 201623:08
//  

#include <stdio.h>

int main(void)
{
	int choice = 0;
	double temperature = 0.0;
	printf("改程序的功能如下:\n"
		"1.将温度从摄氏度转化为华氏度\n"
		"2.将温度从华氏度转化为摄氏度\n"
		"请输入你的选择（1 或 2）");
	scanf("%d", &choice);

	printf("Enter a temperature in degree %s: ", 
		(choice == 1 ? "Centigrade" : "Fahrenheit"));
	scanf("%lf", &temperature);

	if (choice == 1)
		printf("That is equivalent to %.2f degree Fahrenheit\n", temperature*9.0/5.0 + 32.0);
	else
		printf("That is equivalent to %.2f degree Centigrade\n", (temperature-32.0)*5.0/9.0);

	return 0;
}