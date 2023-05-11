#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //For opening the file
    FILE *input_file = fopen(argv[1], "r");

    //If the the input is valid
    if (input_file == NULL)
    {
        printf("Could not open file");
        return 2;
    }

    // Store blocks 512 bytes in array
    unsigned char buffer[512];
    //Track numbers of image recovered
    int count_image = 0;

    //file pointer for recovered images
    FILE *output_file = NULL;

    //Char filename
    char *filename = malloc(8 * sizeof(char));

    //Read the blocks of 512 bytes
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        //Check if bytes represent the start of JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //JPEG filename
            if (count_image > 0)
            {
                fclose(output_file);
            }
            sprintf(filename, "%03i.jpg", count_image);

            // Open output_file for writing
            output_file = fopen(filename, "w");

            //Count number of images found
            count_image++;
        }
        // Check if output has been used for valid input
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }
    free(filename);
    fclose(output_file);
    fclose(input_file);

    return 0;
}