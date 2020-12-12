#include <iostream>

using namespace std;

void MultiplyNumbers()
{
    cout << "Enter the first number: ";
    int firstNumber = 0;
    cin >> firstNumber;

    cout << "Enter the second number: ";
    int secondNumber = 0;
    cin >> secondNumber;

    // Multiply two numbers, store result in a variable
    int multiplicationResult = firstNumber * secondNumber;

    // Display result
    cout << firstNumber << " x " << secondNumber << " = " << multiplicationResult << endl;

}

int main() 
{
    cout << "This program will help you multiply two numbers" << endl;

    MultiplyNumbers();
    return 0;
}
