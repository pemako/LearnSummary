// Program 3.2 using if statements to decide on a discount

#include <stdio.h>

int main(void)
{
	const double unit_price = 3.50;
	int quantity = 0;
	printf("Enter the number that you whant to buy:\n");
	scanf("%d", &quantity);

	// double total = 0.0;
	// if (quantity > 10)
	// 	total = quantity * unit_price * 0.95;
	// else
	// 	total = quantity * unit_price;
	// printf("The price for %d is $%.2f\n", quantity, total);

	double discount = 0.0;

	if (quantity > 10)
		discount = 0.05;

	printf("The price for %d is $%.2f\n", quantity, quantity * unit_price * (1.0 - discount));

	return 0;
}