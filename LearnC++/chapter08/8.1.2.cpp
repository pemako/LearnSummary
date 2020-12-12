#include <iostream>

int main()
{
    int age = 30;
    int *pointsToInt = &age;
    std::cout << "Integer age is at: " << pointsToInt << std::endl;

    return 0;
}
