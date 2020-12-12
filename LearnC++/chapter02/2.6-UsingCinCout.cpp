#include <iostream>

using namespace std;

int main()
{
    int inputNumber;
    cout << "Enter an integer: ";

    // store integer given user input
    cin >> inputNumber;

    // The smae with text i.e. string data
    cout << "Enter you name: ";
    string inputName;
    cin >> inputName;

    cout << inputName << " enterd " << inputNumber << endl;

    return 0;
}
