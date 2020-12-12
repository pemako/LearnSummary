#include <stdio.h>

int main(void)
{
    double value = 0;
    char str[] = "3.5 2.5 1.26";
    char *pstr = str;
    char *ptr = NULL;
    while (1) {
        value = strtod(pstr, &ptr);
        if (pstr == ptr) {
            break;
        } else {
            printf(" %f", value);
            pstr = ptr;
            printf(pstr, &pstr);
        }
    }
    return 0;
}
