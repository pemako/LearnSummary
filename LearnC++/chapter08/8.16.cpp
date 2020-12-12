#include <iostream>

int main()
{
    using namespace std;

    int *pointsToManyNums = new(nothrow) int [0x1fffffffffff];
    if (pointsToManyNums) // check pointsToManyNums != NULL
    {
        // Use the allocated memory
        delete []pointsToManyNums;
    }
    else
        cout << "Memory allocation failed. Ending program " << endl;

    return 0;
}
