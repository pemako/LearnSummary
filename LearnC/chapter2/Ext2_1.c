#include <stdio.h>

int main(void)
{
    float distance = 0.0f;
    // 1英尺是12英寸
    float feet_per_12 = 12;
    // 1码是3英尺
    float yard_per_3  = 3;

    printf("Please input a number of distance： ");
    scanf("%f", &distance);

    printf("Your input number is %f\n", distance);
    printf("Feet number is %f\n", distance / feet_per_12);
    printf("Yard number is %f\n", distance / ( 12 * 3));

    return 0;
}
