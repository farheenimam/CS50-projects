#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int n = get_int("how many scores? ");

    int scores[n];

    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int ("scores: ");
    }
}