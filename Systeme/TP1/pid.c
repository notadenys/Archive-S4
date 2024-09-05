#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(int argc, char ** argv)
{
    printf("%d (parent : %d) : Début de programme\n", getpid(), getppid());
    int tab[1000000]={0}; // tableau de 1 000 000 de cases
    for (int n=0 ; n<10000 ; n++){
        for (int i=0 ; i<1000000 ; i++){
            tab[i]+=1;
        }
        if (n%1000 == 0) { // affichera tous les 1000 où il en est
            printf("%d...\n", n );
        }
    }
    printf("%d (parent : %d) : Fin de programme\n", getpid(), getppid());
    exit(0);
}