#include <iostream>
#include <string>

class Human
{
    private:
        std::string name;
        int age;

    public:
        Human(std::string humansName, int humansAge)
        {
            name = humansName;
            age = humansAge;
            std::cout << "Overloaded constructor creates " << name;
            std::cout << " of age " << age << std::endl;
        }

        void IntroduceSelf()
        {
            std::cout << "I am " + name << " and am ";
            std::cout << age << " years old " << std::endl;
        }
};

int main()
{
    Human firstMan("Adam", 25);
    Human firstWoman("Eve", 28);
    
    firstMan.IntroduceSelf();
    firstWoman.IntroduceSelf();

    return 0;
}
