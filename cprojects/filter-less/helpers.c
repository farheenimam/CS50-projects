#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // For rows and column
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            float Red = image[row][column].rgbtRed;
            float Green = image[row][column].rgbtGreen;
            float Blue = image[row][column].rgbtBlue;

            // For average value
            int avg = round((Red + Green + Blue) / 3.0);
            image[row][column].rgbtRed = image[row][column].rgbtGreen = image[row][column].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // For rows and column
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            float originalRed = image[row][column].rgbtRed;
            float originalGreen = image[row][column].rgbtGreen;
            float originalBlue = image[row][column].rgbtBlue;

            // Calculation for pixels

            int sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            // If value crosses 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // For final values of pixels
            image[row][column].rgbtRed = sepiaRed;
            image[row][column].rgbtGreen = sepiaGreen;
            image[row][column].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // For rows and column
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width / 2; column++)
        {
            RGBTRIPLE temp = image[row][column];
            image[row][column] = image[row][width - (column + 1)];
            image[row][width - (column + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // For copy of image
    RGBTRIPLE temp[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            temp[row][column] = image[row][column];
        }
    }

    for (int row  = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int finalRed, finalGreen, finalBlue;
            finalRed = finalGreen = finalBlue = 0;
            float counter = 0.00;

            // For neighbouring pixels
            for (int m = -1; m < 2; m++)
            {
                for (int n = -1; n < 2; n++)
                {
                    int M = row + m;
                    int N = column + n;

                    if (M < 0 || M > (height - 1) || N < 0 || N > (width - 1))
                    {
                        continue;
                    }

                    // Calculation for image value
                    finalRed += image[M][N].rgbtRed;
                    finalGreen += image[M][N].rgbtGreen;
                    finalBlue += image[M][N].rgbtBlue;

                    counter++;
                }
                // Calculation for average value
                temp[row][column].rgbtRed = round(finalRed / counter);
                temp[row][column].rgbtGreen = round(finalGreen / counter);
                temp[row][column].rgbtBlue = round(finalBlue / counter);

            }
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            image[row][column].rgbtRed = temp[row][column].rgbtRed;
            image[row][column].rgbtGreen = temp[row][column].rgbtGreen;
            image[row][column].rgbtBlue = temp[row][column].rgbtBlue;
        }
    }
    return;
}
