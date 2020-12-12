#include <cstring>
#include <iostream>
#include <string.h>

class MyString
{
    private:
        char *buffer;
    public:
        MyString(const char *initString)
        {
            if (initString != NULL )
            {
                buffer = new char [std::strlen(initString) + 1];
                strcpy(buffer, initString);
            }
            else
                buffer = NULL;
        }

    ~MyString()
    {
        std::cout << "Invoking destructor, clearing up" << std::endl;
        if (buffer != NULL)
            delete []buffer;
    }

    int GetLength() { return std::strlen(buffer); }
    const char *GetString() { return buffer; }
};

int main()
{
    MyString sayHello = "Hello from String Class";
    std::cout << "String buffer in sayHello is " << sayHello.GetLength();
    std::cout << " characters long" << std::endl;
    std::cout << "Buffer contains: " << sayHello.GetString() << std::endl;
}
