//This code is the most compelling way of the recursion
//Implement a lis of numbers as a binary search tree

#include <stdio.h>
#include <stdlib.h>

//Define a node with not one but two pointers
//Represents a node
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

int main (void)
{
    //Tree of size 0
    node *tree = NULL;

    //Add number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    //Initializing node to contain no.2 first
    n->number = 2;
    n->left = NULL;
    n->right = NULL;
    tree = n;

    //Add number to list
    //Here we don't have to initialize node it already exist
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->left = NULL;
    n->right = NULL;
    //Stitching 1 and 2 together
    tree->left = n;

    //Add number to list
    n = malloc(sizeof(node));
    if(n == NULL)
   {
      return 1;
   }
   n->number = 3;
   n->left = NULL;
   n->right = NULL;
   tree->right = n;

    //Print tree
   print_tree(tree);

   //Free tree
   free_tree(tree);
}
   //Free tree function
   void free_tree(node *root)
   {
    if(root == NULL)
    {
        //Return means just quit out of this function
        return;
    }
    //Free left child and right child
    free_tree(root->left);
    free_tree(root->right);
    //Free the address of the root
    //Free this is in the last bcz if we did this in the first we are not not allow to touch right and left child
    free(root);
   }
   //Print tree function will strat at the root node, and recursively print the tree
   //This print function does'nt return anything so void
   void print_tree(node *tree)
   {
    if (root == NULL)
    {
        return;
    }
    //Print the left child
    print_tree(root->left);
    //Print own number
    printf("%i\n", root->number);
    //Print your left child
    print_tree(root->right);
   }
