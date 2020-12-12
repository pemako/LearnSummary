#include <iostream>

void GetSquare(int &number)
{
    number *= number;
}

int main()
{
    using namespace std;
    cout << "Enter a number you wish to square: ";
    int number = 0;
    cin >> number;

    GetSquare(number);
    cout << "Square is: " << number << "====>" << &number << endl;

    return 0;
}
