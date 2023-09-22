// example.c
// $ gcc -o example example.c
// $ ./example

#include <stdio.h>
#include <stdlib.h>

int add(int x, int y)
{
    return x + y;
}

typedef int (*fptr_t)(int, int);

fptr_t get_add_addr(void)
{
    return &add;
}

int call_func_with(fptr_t fptr, int x, int y)
{
    return (*fptr)(x, y);
}

int main(void)
{
    // A function pointer is returned from another function and stored in a
    // variable fptr.
    fptr_t fptr = get_add_addr();
    int value = (*fptr)(3, 5);
    printf("%d\n", value); // 8

    // A function pointer can be passed as an argument to another function.
    value = call_func_with(fptr, 6, 7);
    printf("%d\n", value); // 13

    // Function pointers can be stored in data structures.
    fptr_t array[] = {fptr};

    return EXIT_SUCCESS;
}
