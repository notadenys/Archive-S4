#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>



int main(int argc, char ** argv)
{
    char buffer ;/* buffer d'un seul caractère */
    int descr_tube[2] ;

    pipe(descr_tube) ;/*création d'un tube*/

    pid_t pid;
    switch ( pid = fork() ){
    case (pid_t) (-1) : perror("création impossible");
                        exit(1);
    case (pid_t) 0 : /* on est dans le 1ere processus enfant */
                        printf("Je suis un 1ere enfant!!! %d (parent : %d)\n", getpid(), getppid());
                        fflush(stdout) ;
                        //execl("./recouvrant", argv[1], NULL);
                        perror("Le recouvrement impossible");
                        exit(2);
    default : /* on est dans le processus parent*/
    }

    pid_t pidr;
    switch ( pidr = fork() ){
    case (pid_t) (-1) : perror("création impossible");
                        exit(1);
    case (pid_t) 0 : /* on est dans le 2eme processus enfant */
                        printf("Je suis un 2eme enfant!!! %d (parent : %d)\n", getpid(), getppid());
                        fflush(stdout) ;
                        //execl("./recouvrant", argv[2], NULL);
                        perror("Le recouvrement impossible");
                        exit(2);
    default : /* on est dans le processus parent*/
    }
    exit(0);
}