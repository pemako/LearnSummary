#include <iostream>

int main()
{
    std::cout << "This program will help you multiply two numbers" << std::endl;
    std::cout << "Enter the first number: ";
    int firstNumber = 0;
    std::cin >> firstNumber;

    std::cout << "Enter the second number: ";
    int secondNumber = 0;
    std::cin >> secondNumber;

    // Multiply two numbers, store result in a variable
    int multiplicationResult = firstNumber * secondNumber;

    std::cout << firstNumber << " x " << secondNumber ;
    std::cout << " = " << multiplicationResult << std::endl;

    return 0;
}
