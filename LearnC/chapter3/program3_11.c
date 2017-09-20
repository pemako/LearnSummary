// author <pemakoa@gmail.com>
// Jun 13, 201622:54
// 简单的计算器 用户输入 number1 操作符 number2 返回计算的结果

#include <stdio.h>

int main(void)
{
	double number1 = 0.0;
	double number2 = 0.0;
	char operation = 0; // Must be + - * / %

	printf("请输入计算： 如 2 + 3:\n");	
	scanf("%lf %c %lf", &number1, &operation, &number2);

	switch(operation){
		case '+':
			printf("= %lf \n", number1 + number2);
			break;
		case '-':
			printf("= %lf \n", number2 + number1);
			break;
		case '*':
			printf("= %lf \n", number1 * number2);
			break;
		case '/':
			if (number2 == 0)
				printf("\n\n 被除数不能为0\n");
			else
				printf("= %lf \n", number1 / number2);
			break;
		case '%':
			if ((long)number2 == 0)
				printf("\n\n 被除数不能为0\n");
			else
				printf("= %ld \n", (long)number1 % (long)number2);
			break;
		default:
			printf("请输入正确的操作符\n");
			break;
	}

	return 0;
}