#include <iostream>

int main()
{
    int age = 30;
    int *pointsToInt = &age;
    std::cout << "PointsToInt points to age now" << std::endl;

    std::cout << "pointsToInt = " << pointsToInt << " 值为：" << *pointsToInt << std::endl;

    int dogsAge = 9;
    pointsToInt = &dogsAge;
    std::cout << "pointsToInt points to dogsAge now" << std::endl;
    std::cout << "pointsToInt = " << pointsToInt << " 值为：" << *pointsToInt << std::endl;

    return 0;
}
