#include <iostream>
#include <string>

class Human
{
    private:
        std::string name;
        int age;

    public:
        Human()
        {
            age = 0;
            std::cout << "Default constructor: name and age not set" << std::endl;
        }

        Human(std::string humansName, int humansAge)
        {
            name = humansName;
            age = humansAge;
            std::cout << "Overloaded constructor creates ";
            std::cout << name << " of " << age << " years" << std::endl;
        }
};

int main()
{
    Human firstMan;
    Human firstWoman("Eve", 20);
}
