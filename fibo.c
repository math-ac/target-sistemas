#include <stdio.h>

long int fibonacci(long int number)
{
    if (number == 0)
        return 0;
    else if (number == 1)
        return 1;
    else
        return fibonacci(number - 1) + fibonacci(number - 2);
}


int main(void)
{
    long int number, i = 0;;
    int flag = 0;

    printf("Este número pertence a sequencia?\n");
    scanf("%ld", &number);

    while (flag == 0) {
        if (fibonacci(i) == number)
            flag = 1;
        if (fibonacci(i) > number)
            flag = 2;
        i++;
    }

    if (flag == 2)
        printf("O número %ld não pertence a sequencia de Fibonacci\n", number);
    else
        printf("O número %ld pertence a sequencia de Fibonacci\n", number);

    return 0;
}
