#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv)
{
    printf("%d (parent : %d)\n", getpid(), getppid());
    fflush(stdout) ;
    pid_t ret;
    switch ( ret = fork() ){
    case (pid_t) -1 :   perror("création impossible");
                        exit(1);
    case (pid_t) 0 :
                        printf("Je suis un enfant!!! %d (parent : %d)\n", getpid(), getppid());
                        fflush(stdout) ;
                        break;
    default :
    printf("%d (parent : %d)\n", getpid(), getppid());
    fflush(stdout) ;
    return 0;
    }
}