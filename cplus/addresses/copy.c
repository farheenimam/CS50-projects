#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main (void)
{
    string s = get_string("s: ");

    string t = s;

     if (strlen(t) > 0)
    {
        t[0] = toupper (t[0]);
    }
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}

*The problem in this program is that we want to capitalize only the word in 't' not the 's' one also, so the solution
is in malloc.c