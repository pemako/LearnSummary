#include <iostream>

int main()
{
    using namespace std;

    int original = 30;
    cout << "original = " << original << endl;
    cout << "original is at address: " << &original << endl;

    int &ref1 = original;
    cout << "ref1 is at address: " << &ref1 << endl;

    int &ref2 = ref1;
    cout << "ref2 is at address: " << &ref2 << endl;
    cout << "Therefore, ref2 = " << ref2 << endl;

    return 0;
}
