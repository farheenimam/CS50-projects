//This code is the most compelling way of the recursion
//Implement a lis of numbers as a binary search tree

#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;
int main(void)
{
    // Tree of size 0
    node *tree = NULL;

    // Add number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 2;
    n->left = NULL;
    n->right = NULL;
    tree = n;

   // Add number to list
   n = malloc(sizeof(node));
   if (n == NULL)
   {
      free_tree(tree);
      return 1;
   }
   n->number = 1;
   n->left = NULL;
   n->right = NULL;
   tree->left = n;

   // Add number to list
   n = malloc(sizeof(node));
   if (n == NULL)
   {
   free_tree(tree);
   return 1;
   }
   n->number = 3;
   n->left = NULL;
   n->right = NULL;
   tree->right = n;

// Print tree
print_tree(tree);

// Free tree
free_tree(tree);
return 0;
}

void free_tree(node *root)
   {
    if(root == NULL)
    {
        return 1;
    }

    free_tree(root->left);
    free_tree(root->right);
    free(root);
   }

  void print_tree(node *root)
{
    if (root == NULL)
    {
        return 1;
    }
    print_tree(root->right);
    printf("%i\n", root->number);
    print_tree(root->left);
}



