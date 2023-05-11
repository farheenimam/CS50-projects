// BMP files, another format for images
// Have even more bytes in its header, or begining of the file
#include "helpers.h"

// Version of image filters that only shows the red color
// Only let red through
void filter(int height, int width, RGBTRIPLE image [height][width])
{
    // A lops that iterate over all the in a two-dimensional array
    //Sets blue and green value to zero
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Setting blue and green values to zero
            image[i][j].rgbtBlue = 0x00;
            imgae[i][j].rgbtGreen = 0x00;
        }
    }
}