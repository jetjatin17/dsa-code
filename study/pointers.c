// today we will learn pointers.

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int num = 69;
    int *ptr = &num;
    printf("%d is good",ptr);

    return 0;
}