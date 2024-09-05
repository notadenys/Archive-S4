#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int main(int argc, char ** argv)
{
    struct stat s;
    char ref[1024];
    strcpy(ref, argv[1]);
    if(stat(ref, &s)==-1) {
        perror("Le fichier/répertoire n'existe pas\n");
        exit(1);
    }
    if(S_ISREG(s.st_mode))
    {
        printf("<%s> est un fichier (i-node %ld)\n", ref, s.st_ino);
        printf("--> taille : %.2f Ko\n", (float)s.st_size/1024.);
        printf("--> modif le %s", ctime(&s.st_mtime));
        printf("--> access le %s", ctime(&s.st_atime));

        printf("=====Extrait=======\n");
        int file = open(ref, O_RDONLY);
        int i = 0;
        char buf;
        while(i<100 && read(file, &buf, sizeof(char)))
        {
            printf("%c", buf);
            i++;
        }
        close(file);
        printf("\n===================\n");
    } 
    else if (S_ISDIR(s.st_mode))
    {
        printf("<%s> est un répertoire (i-node %ld)\n", ref, s.st_ino);
        printf("--> taille : %.2f Ko\n", (float)s.st_size/1024.);
        printf("--> modif le %s", ctime(&s.st_mtime));
        printf("--> access le %s", ctime(&s.st_atime));
    }
    return 0;
}