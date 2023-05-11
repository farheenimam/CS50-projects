// Point from one chunk of memory to another
#include <stdio.h>
#include <stdlib.h>

//initializing original array of size 3
int main (void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

//Time passes and we need more space

//Ask comp for second chunk of memory
//Resize old array to be of size 4
 int *tmp = realloc(list, 4 * sizeof(int));

// For safety check if tmp equals to null just quiet programm
 if (tmp == NULL)
{
  // Free old array
    free(list);
    return 1;
}
// Copy from old array into new array
 tmp[3] = 4;
// Remember new array
// Here we are pointing at the new chunk of memory 'tmp'
  list = tmp;

  // Print new array
  for (int i = 0;i < 4; i++)
  {
    printf("%i\n", list[i]);
  }
  //Free new array
  free(list);
  return 0;
}