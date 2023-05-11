#include <stdio.h>

int main (void)
{
    int m[] = {9, 8 , 5, 7, 2 ,3};

    printf("%i\n", *(m+4));
    printf("%i\n", *(m+5));
    printf("%i\n", *(m+2));
    printf("%i\n", *(m+3));
    printf("%i\n", *(m+1));
    printf("%i\n", *m);
}