#include <stdio.h>
#include <ctype.h>

int main (void)
{
    int n = 0; int m = 0;
    {
        printf("Input Two Digits, specify with space: ");
        scanf("%i", &m);
        scanf("%i", &n);
        if (!isdigit(m) || !isdigit(n))
        {
            printf("Not a digit\n");
        }
        else
        {
            return 0;
        }

        int o = 0;
        while (o < 1 || o > 5)
        {
            printf("1 For '+', 2 For '-', 3 For '/', 4 For '*'\n");
            printf("Write the correct no. for your opreator: ");
            scanf("%i", &o);
            if (!isdigit(o))
            {
                return 1;
            }
        }

            switch(o)
            {
                case 1:
                printf("%i + %i = %i\n", m, n, n + m);
                break;
                case 2:
                printf("%i - %i = %i\n", m, n, n - m);
                break;
                case 3:
                printf("%i / %i = %f\n", m, n, (float)m/(float)n);
                break;
                case 4:
                printf("%i * %i = %i\n", m, n, n * m);
                break;
            }
    }
}