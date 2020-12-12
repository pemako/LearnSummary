#include <iostream>

int main()
{
    using namespace std;

    char sayHello[] = {'H','e','l','l','o',' ','W','o','r','l','d','\0'};
    cout << sayHello << endl;
    cout << "Size of array: " << sizeof(sayHello) << endl;

    cout << "Replaceing space with null " << endl;
    sayHello[5] = '\0';
    cout << sayHello << endl;
    cout << "Size of array: " << sizeof(sayHello) << endl;

    return 0;
}
