#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int n = get_int("n: ");
    switch(n)
    {
        case 1:
        printf("one!\n");
        break;
        case 2:
        printf("two\n");
        break;
        case 3:
        printf("three\n");
        break;
        case 4:
        printf("four\n");
        break;
        default:
        printf("sorry get out!\n");
    }
}