#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main(int argc, char ** argv)
{
    printf("%d (parent : %d)\n", getpid(), getppid());
    fflush(stdout) ;

    int tab[4] = {1, 1, 1, 1};

    pid_t pid;
    switch ( pid = fork() ){
    case (pid_t) (-1) : perror("création impossible");
                        exit(1);
    case (pid_t) 0 : /* on est dans le 1ere processus enfant */
                        printf("Je suis un enfant!!! %d (parent : %d)\n", getpid(), getppid());
                        fflush(stdout) ;
                        for (int i = 0; i < 4; i++) {tab[i] = 4;}
                        sleep(2);
                        printf("Adresse de tableau : %p\n", &tab);
                        for (int i = 0; i < 4; i++) {printf("%d\n",tab[i]);}
                        perror("Le recouvrement impossible");
                        exit(2);
    default : /* on est dans le processus parent*/
    }
    for (int i = 0; i < 4; i++) {printf("%d\n",tab[i]);}
    for (int i = 0; i < 4; i++) {tab[i] = 2;}
    int status = 0;
    int* pStatus = &status;
    wait(pStatus);
    printf("Adresse de tableau : %p\n", &tab);
    for (int i = 0; i < 4; i++) {printf("%d\n",tab[i]);}
    exit(0);
}