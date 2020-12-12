#include <iostream>

enum YourCards {Ace = 43, Jack, Queen, King};

int main()
{
    YourCards myTest = Queen;

    std::cout << myTest << std::endl; 
    return 0;
}
