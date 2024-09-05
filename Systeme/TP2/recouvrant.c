#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>
#include <errno.h>   // for errno
#include <limits.h>  // for INT_MAX, INT_MIN


int main(int argc, char ** argv)
{
    char *p;
    int num;

    errno = 0;
    long conv = strtol(argv[0], &p, 10);

    // Check for errors: e.g., the string does not represent an integer
    // or the integer is larger than int
    if (errno != 0 || *p != '\0' || conv > INT_MAX || conv < INT_MIN) {
        perror("ERROR");
        exit(1);
    } else {
        // No error
        num = conv;
        printf("J'attends %d sec\n", num);
        sleep(num);
        printf("Je suis un enfant!!! %d (parent : %d)\n", getpid(), getppid());
        fflush(stdout) ;
    }
    return num;
}