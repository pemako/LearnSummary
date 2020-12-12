#include <stdio.h>

int main(void)
{
    int grades[10];
    unsigned int count = 10;
    long sum = 0L;
    float average = 0.0f;

    printf("\nEnter the 10 grades:\n");
    for(unsigned int i = 0; i<count; ++i)
    {
        printf("%2u> ", i + 1);
        scanf("%d", &grades[i]);
        sum += grades[i];
    }

    average = (float)sum/count;

    printf("\nAverage of the ten grades entered is: %f\n", average);
    return 0;
}
