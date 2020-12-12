#include <iostream>

int main()
{
    int age = 30;
    const double Pi = 3.1416;

    std::cout << "Integer age is located at :0x" << &age << std::endl;
    std::cout << "Double Pi is located at :0x" << &Pi << std::endl;
    return 0;
}
