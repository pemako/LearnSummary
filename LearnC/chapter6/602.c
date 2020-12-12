#include <stdio.h>

int main(void)
{
    char str1[] = "To be or not to be";
    char str2[] = ",that is the question";
    unsigned int count = 0;

    while(str1[count] != '\0')
        ++count;

    printf("The lengthe of the string \"%s\" is %d characters.\n", str1, count);

    count = 0;
    while(str2[count])
        count++;

    printf("The lengthe of the string \"%s\" is %d characters.\n", str2, count);
    return 0;
}
