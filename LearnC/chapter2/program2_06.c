#include <stdio.h>

int main(void)
{
    int cookies = 45;
    int children = 7;
    int cookies_per_child = 0;
    int cookies_left_over = 0;

    cookies_per_child = cookies / children;

    printf("You have %d children and %d cookies\n", children, cookies);
    printf("Give each child %d cookies.\n", cookies_per_child);

    cookies_left_over = cookies % children;
    printf("There are %d cookies left over \n", cookies_left_over);
    
    return 0;
}
