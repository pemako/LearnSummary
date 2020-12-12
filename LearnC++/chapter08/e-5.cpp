#include <iostream>

int main()
{
    using namespace std;
    int *pointToAnInt = new int [0x1fffffff];
    int *pNumberCopy = pointToAnInt;
    *pNumberCopy = 30;

    cout << *pointToAnInt;
    delete pNumberCopy;

    return 0;
}
