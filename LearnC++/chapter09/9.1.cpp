#include <iostream>
#include <string>

class Human
{
    public:
        std::string name;
        int age;

    void IntroduceSelf()
    {
        std::cout << "I am " + name << " and am ";
        std::cout << age << " years old " << std::endl;
    }

};

int main()
{
    Human firstMan;
    firstMan.name = "Adam";
    firstMan.age = 30;

    Human firstWoman;
    firstWoman.name = "Eve";
    firstWoman.age = 28;

    firstMan.IntroduceSelf();
    firstWoman.IntroduceSelf();
}
