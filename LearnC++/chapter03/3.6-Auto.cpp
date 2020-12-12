#include <iostream>

int main()
{
    using namespace std;
    
    // 使用auto的时候必须对变量进行初始化，如果不初始化则会编译出错
    auto coinFlippedHeads = true;
    auto largeNumber = 2500000000000;

    cout << "coinFlippedHeads = " << coinFlippedHeads;
    cout << ", sizeof(coinFlippedHeads) = " << sizeof(coinFlippedHeads) << endl;

    cout << "largeNumber = " << largeNumber;
    cout << ", sizeof(largeNumber) = " << sizeof(largeNumber) << endl;

    return 0;
}
