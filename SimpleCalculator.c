#include <stdio.h>

int taking_input(void);
int calculation(int number1, int number2, char option);
char operation(void);

int main(void)
{
    int a = taking_input();
    int b = taking_input();
    char option = operation();

    printf("Ans: %i\n", calculation(a, b, option));
}

int taking_input(void)
{
    int number;
    printf("Enter a number: ");
    scanf("%i", &number);
    return number;
}

int calculation(int number1, int number2, char option)
{
    int result;
    switch (option)
    {
        case 'a':
            result = number1 + number2;
            break;
        case 'b':
            result = number1 - number2;
            break;
        case 'c':
            result = number1 * number2;
            break;
        case 'd':
            result = number1 / number2;
            break;
    }
    return result;
}

char operation(void)
{
    char c;
    printf("Choose what to do.\na.addition\nb.substruction\nc.multiplication\nd.division\n");
    scanf(" %c", &c);
    return c;
}
