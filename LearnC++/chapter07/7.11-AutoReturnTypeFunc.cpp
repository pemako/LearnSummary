#include <iostream>

using namespace std;

const double Pi = 3.14159265;

// auto 对函数类型推断的时候需要C++14才支持
auto Area(double radius)
{
    return Pi * radius * radius;
}

int main() 
{
    cout << "Enter radius: ";
    double radius = 0;
    cin >> radius;

    cout << "Area is: " << Area(radius) << endl;

    return 0;
}
