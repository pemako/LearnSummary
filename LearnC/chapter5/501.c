#include <stdio.h>

int main(void)
{
    int grade = 0;
    unsigned int count = 10;
    long sum = 0L;
    float average = 0.0f;

    for(unsigned int i = 0; i < count; ++i)
    {
        printf("Enter a agrade: ");
        scanf("%d", &grade);
        sum += grade;
    }

    average = (float)sum / count;

    printf("\nAverage of the ten grades entered is: %f\n", average);
    return 0;
}
