//This code prints out 1,2,3
//Example of linked list
#include <stdio.h>
#include <stdlib.h>

//Declaring the function of node
typedef struct node
{
    int number;
    struct node *next;
}
node;
int main (void)
{
    //List of size
    node *list = NULL;

    //Add a number to list
    //Declaring variable 'n'
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next = NULL;

    //Upgate the list to point to new node
    list = n;

    //Add anumber to list
    n = malloc(sizeof(node));

    //safety check
    if(n == NULL)
    {
      free(list);
      return 1;
    }
    n->number = 2;
    n->next = NULL;
    //We tell the computer to 'list' feild's 'next' field and store address
    list->next = n;

    //Add number to list
    //On line#20 we had already define the variable so no need
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n;

    //Print the numbers
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }

    //Free list
    while (list != NULL)
   {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return 0;
}