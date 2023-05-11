#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    string name = get_string("NAME: ");
    printf("Thanks %s for your cooperation\n", name);
}
