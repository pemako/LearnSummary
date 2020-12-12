#include <iostream>

void GetSquare(const int &number, int &result) { result = number * number; }

int main()
{
    using namespace std;
    cout << "Enter a number you wish to square: ";
    int number = 0;
    cin >> number;

    int square = 0;
    GetSquare(number, square);
    cout << number << "^2 = " << square << endl;
    return 0;
}
