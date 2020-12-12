#include <iostream>
#include <string>

class Human
{
    private:
        std::string name;
        int age;

    public:
        Human(std::string humansName = "Adam", int humansAge = 25) 
            :name(humansName), age(humansAge)
        {
            std::cout << "Constructed a human called " << name;
            std::cout << ", " << age << " years old" << std::endl;
        }

};

int main()
{
    Human adam;
    Human eve("Eve", 18);

    return 0;
}
