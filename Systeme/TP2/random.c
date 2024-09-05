#define N 300

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main(int argc, char ** argv)
{
    printf("%d (parent : %d)\n", getpid(), getppid());
    fflush(stdout) ;

    int * tab = (int*) malloc(N*sizeof(int));
    srand(getpid());
    for (int i = 0; i < N; i++) {tab[i] = rand()%20;}

    pid_t pid;
    switch ( pid = fork() ){
    case (pid_t) (-1) : perror("création impossible");
                        exit(1);
    case (pid_t) 0 : /* on est dans le 1ere processus enfant */
                        printf("Je suis un enfant!!! %d (parent : %d)\n", getpid(), getppid());
                        fflush(stdout);
                        perror("Le recouvrement impossible");
                        exit(2);
    default : /* on est dans le processus parent*/
    }
    exit(0);
}