#include <cs50.h>
#include <stdio.h>

int main (void)
{
   int f = get_int("Subjects: ");

   int marks[f];

   for (int i = 0; i < f; i++)
   {
     marks[i] = get_int("Marks: ");
   }
}
