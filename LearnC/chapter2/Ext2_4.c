#include <stdio.h>

int main(void)
{
    double week_salary = 0.0;
    double work_hourys = 0.0;

    int dollars = 0;
    int cents = 0;

    printf("请输入一周的薪水，单位为美元: ");
    scanf("%lf", &week_salary);
    printf("请输入每周工作时间,单位为小时: ");
    scanf("%lf", &work_hourys);

    dollars = (int)(week_salary / work_hourys);

    cents = (int)(100.0 * (week_salary / work_hourys - dollars) + 0.5);

    printf("Your average hourly pay rate is %d dollars and %d cents.\n",dollars, cents);

    return 0;

}
