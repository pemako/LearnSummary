#include <iostream>

int main()
{
    using namespace std;

    try 
    {
        int *pointsToManyNums = new int [0x1fffffff];
        delete []pointsToManyNums;
    }
    catch (bad_alloc)
    {
        cout << "Memory allocation failed. Ending program " << endl;
    }

    return 0;
}
