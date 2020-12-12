#include <stdio.h>

int main(void)
{
#if defined __STDC_LIB_EXT1__
    printf("Optional functions are defined.\n");
#else
    printf("Optional functions are not defined.\n");
#endif
    return 0;
}
