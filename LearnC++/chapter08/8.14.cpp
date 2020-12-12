#include <iostream>

int main()
{
    using namespace std;
    cout << "Is it sunny (y/n)? ";
    char userInput = 'y';
    cin >> userInput;

    bool * const isSunny = new bool;
    *isSunny = true;

    if (userInput == 'n')
        *isSunny = false;

    cout << "Boolean flag sunny syas: " << *isSunny << endl;
    delete isSunny;

    return 0;
}
