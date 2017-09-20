#include <stdio.h>

int main(void)
{
    float radius = 0.0f;
    float diameter = 0.0f;
    float circumfrerence = 0.0f;
    float area = 0.0f;
    const float Pi = 3.1415926;

    printf("Input the diameter of the table:");
    scanf("%f", &diameter);

    radius = diameter / 2.0f;
    circumfrerence = 2.0f * Pi * radius;
    area = Pi * radius * radius;

    printf("\nThe circumfrerence is %.2f", circumfrerence);
    printf("\nThe area is %.2f\n", area);

    return 0;
}
