#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(int argc, char ** argv)
{
    srand(time(NULL));
    printf("%d\n", (int)((rand() / (float) RAND_MAX ) * 2));
    exit(0);
}