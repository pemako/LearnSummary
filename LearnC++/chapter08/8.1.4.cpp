#include <iostream>

int main()
{
    using namespace std;

    int dogsAge = 30;
    cout << "Initialized dogsAge = " << dogsAge << endl;
    int *pointsToAge = &dogsAge;
    cout << "pointsToAge points to dogsAge " << endl;
    cout << "Enter an age for your dog: ";
    cin >> *pointsToAge;

    cout << "Input stored at " << pointsToAge << endl;
    cout << "Integer dogsAge = " << dogsAge << endl;
}
