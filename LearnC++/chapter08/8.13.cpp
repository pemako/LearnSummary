#include <iostream>

int main()
{
    using namespace std;
    bool *isSunny;
    cout << "Is it sunny (y/n)? ";
    char userInput = 'y';
    cin >> userInput;

    if (userInput == 'y')
    {
        isSunny = new bool;
        *isSunny = true;
    }

    cout << "Boolena flag sunny says: " << *isSunny << endl;
    delete isSunny;

    return 0;
}
