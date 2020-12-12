#include <iostream>

int main()
{
    using namespace std;
    // Static array of 5 integers
    int myNumbers[5];

    // array assigned to pointer to int
    int *pointToNums = myNumbers;

    // Display address contained in pointer
    cout << "pointToNums = " << pointToNums << endl;

    // Address of first element of array
    cout << "&myNumbers[0] = " << &myNumbers[0] << endl;
    cout << "&myNumbers[1] = " << &myNumbers[1] << endl;
    cout << "&myNumbers[2] = " << &myNumbers[2] << endl;

    return 0;
}
