#include <stdio.h>
#include <ctype.h>

int main (void)
{
    int n = 0;
    {
        printf("Number: ");
        scanf("%i", &n);

        if (n == isdigit(n))
        {
            printf("Please type a number\n");
        }
        else if (n % 2 == 0)
        {
            printf("Even\n");
        }
        else
        {
            printf("Odd\n");
        }
    }
}