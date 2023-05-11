// Detects if a file is jpg
#include <stdint.h>
#include <stdio.h>

// Assigning a type, defined in stdint.h, representing an 8-bit unsigned integer
// To create a new type to store a byte of data,
// You can do so via the below, which defines a new type called BYTE
typedef uint8_t BYTE;

// For getting 2 argument
int main(int argc, char *argv[])
{
    // Check usage
    if (argc != 2)
    {
        printf("If u know write properly,stupid!\n");
        return 1;
    }

    // For opening a file use this
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }
    if (file == NULL)
    {
        printf("empty\n");
    }
  // Read first three bytes from a file with a function called fread
  BYTE bytes[3];
  // Comparing first three bytes(in hexadecimal) to the three bytes required to begin a jpg file
  fread(bytes, sizeof(BYTE), 3, file);

  // Check first three bytes
  //If they are same then jpg
  if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
  {
    printf("Yes found jpg file\n");
  }
  // If they are not jpg file
  else
  {
    printf("No! Get lost\n");
  }

  // Close the file now
  fclose(file);
}