#include <stdio.h>

int main(void)
{
    /*
    float standard_price = 3.5;
    float deluxe_price = 5.5;
    char flag;
    int number = 0;
    float total_price = 0.0f;

    printf("请输入选择的版本 A:标准版, B: 豪华版" );
    scanf("%c",&flag);
    printf("请输入购买的数量: ");
    scanf("%d", &number);

    if (flag == 'A') {
        printf("总价钱为：%.2f\n", standard_price * number);
    } else if(flag == 'B') {
         printf("总价钱为: %.2f\n", deluxe_price * number);
    } else {
        printf("请选择正确的版本");
    }

    */
    double total_price = 0.0;
    int type = 0;
    int quantity = 0;
    const double type1_price = 3.50;
    const double type2_price = 5.50;

    printf("Enter the type (1 or 2): ");
    scanf("%d", &type);

    printf("Enter the quantity: ");
    scanf("%d", &quantity);

    total_price = quantity * (type1_price + (type - 1) * (type2_price - type1_price));

    printf("The price for %d of type %d is $%.2f\n", quantity, type, total_price);
}


    
