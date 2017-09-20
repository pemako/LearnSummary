#include <stdio.h>

int main(void)
{
    const float Revenue_Per_150 = 4.5f;
    short JanSold = 23500;
    short FebSold = 19300;
    short MarSold = 21600;
    float RevQuarter = 0.0f;

    //short QuarterSold = JanSold + FebSold + MarSold;
    unsigned long QuarterSold = JanSold + FebSold + MarSold;

    printf("Stock sold in\n Jan:%d\nFeb: %d\nMar: %d\n", JanSold, FebSold, MarSold);

    //printf("Total stock sold in first quarter: %d\n", QuarterSold); // -1136
    printf("Total stock sold in first quarter: %lu\n", QuarterSold); // -1136

    //RevQuarter = QuarterSold / 150 * Revenue_Per_150 ;
    RevQuarter = QuarterSold * Revenue_Per_150 / 150;
    printf("Sales revenue this quarter is : $%.2f\n", RevQuarter);

    return 0;
}
