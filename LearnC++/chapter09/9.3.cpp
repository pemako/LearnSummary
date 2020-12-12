#include <iostream>
#include <string>

class Human
{
    private:
        std::string name;
        int age;

    public:
        Human() // constructor
        {
            age = 1;
            std::cout << "Constructed an instance of class Human " << std::endl;
        }

        void SetName(std::string humansName) { name = humansName; }
        void SetAge(int humansAge) { age = humansAge; }
        void IntroduceSelf()
        {
            std::cout << "I am " + name << " and am ";
            std::cout << age << " years old " << std::endl;
        }
};

int main()
{
    Human firstWoman;
    firstWoman.SetName("Eve");
    firstWoman.SetAge(28);
    firstWoman.IntroduceSelf();

    return 0;
}
