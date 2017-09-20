#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(void)
{
    printf("Variables of type char short value from %d to %d \n", CHAR_MIN, CHAR_MAX);
    printf("Variables of type unsigned char store value from 0 to %u \n", UCHAR_MAX);

    return 0;
}
