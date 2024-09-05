#include <dirent.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>


int main(int argc, char ** argv)
{
    struct dirent * d;
    struct stat s;
    char ref[1024];
    strcpy(ref, argv[1]);

    DIR * dir = opendir(ref);
    if(dir == NULL) {
        perror("Le répertoire n'existe pas : \n");
        exit(1);
    }

    float taille = 0;
    d = readdir(dir);
    while(d != NULL)
    {
        stat(d->d_name, &s);
        if(S_ISREG(s.st_mode))
        {
            printf("<%s/%s> est un fichier (i-node %ld)\n", ref, d->d_name, d->d_ino);
            taille += s.st_size;
        }
        else if (S_ISDIR(s.st_mode))
        {
            printf("<%s/%s> est un répertoire (i-node %ld)\n", ref, d->d_name, d->d_ino);
        }
        d = readdir(dir);
    }
    printf("Taille du répertoire : %.2f Ko\n", taille/1024.);
    closedir(dir);
    
    return 0;
}