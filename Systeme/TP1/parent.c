#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>


int main(int argc, char ** argv)
{
    printf("%d (parent : %d)\n", getpid(), getppid());
    fflush(stdout) ;

    pid_t ret;
    switch ( ret = fork() ){
    case (pid_t) (-1) :   perror("création impossible");
                        exit(1);
    case (pid_t) 0 : /* on est dans le processus enfant */
    printf("Je suis un enfant!!! %d (parent : %d)\n", getpid(), getppid());
    fflush(stdout) ;
    execl("./recouvrant", argv[1], argv[2], NULL);
    perror("Le recouvrement impossible");
    exit(2);
    default : /* on est dans le processus parent*/
    }
    exit(0);
}