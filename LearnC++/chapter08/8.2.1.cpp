#include <iostream>

int main()
{
    using namespace std;
    // Request for memory space for an int
    int *pointsToAnAge = new int;
    
    // Use the allocated memory to store a number
    cout << "Enter your dog's age: ";
    cin >> *pointsToAnAge;

    // use indirection operator* to access value
    cout << "Age " << *pointsToAnAge << " is stored at 0x" << pointsToAnAge << endl;
    delete pointsToAnAge;

    return 0;
}
