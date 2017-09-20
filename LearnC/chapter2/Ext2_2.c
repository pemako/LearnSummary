#include <stdio.h>

int main(void)
{
    float height = 0.0f;
    float width = 0.0f;
    float area = 0.0f;

    int feet_per_12 = 12;
    int yard_per_3 = 3;
    printf("请输入一个房间的长度单位为英尺: ");
    scanf("%f", &height);
    printf("请输入一个房间的宽度单位为英寸：");
    scanf("%f", &width);

    area = (height / yard_per_3) * (width / (feet_per_12 * yard_per_3));

    printf("Area is %.2f\n", area);
}
