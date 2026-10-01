// structure.

#include<stdio.h>
#include<stdlib.h>

struct student{
    char name[20];
    int id;
    int marks[3];
    int average;
};

// typedef struct name n;

int main(){
    struct student n1;
    n1.id = 5;
    printf("%d",n1.id);
    return 0;
}
