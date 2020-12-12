#include <iostream>
#include <string>

int main()
{
    using namespace std;

    cout << "How many integers shall I reserve memory for?" << endl;
    int numEntries = 0;
    cin >> numEntries;

    int *myNumbers = new int[numEntries];

    cout << "Memory allocated at:" << myNumbers << endl;
}
