#include <iostream>

class Human
{
    private:
        int age;
    public:
        void SetAge(int inputAge) { age = inputAge; }
        int GetAge()
        {
            if (age > 30)
                return (age - 2);
            else
                return age;
        }
};

int main()
{
    Human firstMan;
    firstMan.SetAge(35);

    Human firstWoman;
    firstWoman.SetAge(22);

    std::cout << "Age of firstMan " << firstMan.GetAge() << std::endl;
    std::cout << "Age of firstWoman " << firstWoman.GetAge() << std::endl;

    return 0;
}

