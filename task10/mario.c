#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height, i, column, space;
    do
    {
        height = get_int("Enter height:");
    }
    while (height < 1 || height > 8);

    for (i = 0; i < height; i++)
    {
        for (space = 0; space < height - i - 1; space++)
        {
            printf(" ");
        }
        for (column = 0; column <= i; column++)
        {
            printf("#");
        }
        printf("\n");
    }
}