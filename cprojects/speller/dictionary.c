// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// For the variables
unsigned int hashvalue;
unsigned int word_count;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // For hash value
    hashvalue = hash(word);

    // For cursor to point at the node
    node *cursor = table[hashvalue];
    while (cursor != 0)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // With reference of Sir Dougg's Hash Table in the class
    int sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        sum += tolower(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // To open the file
    FILE *file = fopen(dictionary, "r");

    // Safety check if the file could not be accessed
    if (file == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }

    // To read words from the file
    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        // Getting memeory for the node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        // To copy the word into the node
        strcpy(n->word, word);

        // For hash value
        hashvalue = hash(word);

        n->next = table[hashvalue];
        table[hashvalue] = n;
        word_count++;
    }
    // To close file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // To go through each bucket
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        // To free
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
        if (cursor == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
