#include <stdio.h>
#define PI 3.14159f

int main(void)
{
    float radius = 0.0f;
    float diameter = 0.0f;
    float circumfrerence = 0.0f;
    float area = 0.0f;

    printf("Input the diameter of the table:");
    scanf("%f", &diameter);

    radius = diameter / 2.0f;
    circumfrerence = 2.0f * PI * radius;
    area = PI * radius * radius;

    printf("\nThe circumfrerence is %.2f", circumfrerence);
    printf("\nThe area is %.2f\n", area);

    return 0;
}