#include <stdio.h>
#include <math.h>
int main(void)
{
    int n = 0;
    while (n < 1 || n > 12)
    {
        printf("Enter a digit: ");
        scanf("%i", &n);
    }

    for (int m = 1; m <= 12; m++)
    {
        printf("%i * %i = %i\n", n, m, n * m);
    }
}