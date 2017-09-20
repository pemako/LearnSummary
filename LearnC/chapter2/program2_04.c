// Program 2.4 simple calculations

#include <stdio.h>

int main(void)
{
    int total_pets;
    int cats;
    int dogs;
    int ponies;
    int others;

    // set the number of each kind of pet
    cats = 2;
    dogs = 1;
    ponies = 1;
    others = 46;

    total_pets = cats + dogs + ponies + others;

    printf("We have %d pets in total\n", total_pets);
    return 0;
}
