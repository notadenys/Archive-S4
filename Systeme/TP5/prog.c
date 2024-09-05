#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char ** argv)
{
    struct stat s;
    char ref[1024];
    char copie[1024] = "(copy)";
    strcpy(ref, argv[1]);
    strcat(copie, ref);

    if(stat(ref, &s)==-1) {
        perror("Le fichier/répertoire n'existe pas");
        exit(1);
    }
    if(S_ISREG(s.st_mode))
    {
        int fileR = open(ref, O_RDONLY);
        int i = 0;
        char buf;
        read(fileR, &buf, sizeof(char));
        char b = buf;
        read(fileR, &buf, sizeof(char));
        char m = buf;
        if( b == 'B' && m == 'M' )
        {
            int buff;
            for (int i = 0; i < 3; i++)
            {
                read(fileR, &buff, sizeof(int));
            }
            int offset;
            read(fileR, &offset, sizeof(int));
            int width;
            read(fileR, &width, sizeof(int));
            int height;
            read(fileR, &height, sizeof(int));
            short bpp;
            read(fileR, &bpp, sizeof(short));
            read(fileR, &bpp, sizeof(short));
            int compression;
            read(fileR, &compression, sizeof(int));

            printf("Le fichier : %s\nwidth : %d\nheight : %d\nbits par pixel : %hu\ncompression : %s\n", ref, width, height, bpp, compression ? "oui" : "non");


            lseek(fileR, 0, SEEK_SET);
            int fileW = open(copie, O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
            int oct_lu = 0;
            while(oct_lu < offset)
            {
                oct_lu += read(fileR, &buf, sizeof(char));
                write(fileW, &buf, 1);
                i++;
            }
            close(fileW);
        }
        else
        {
            printf("Le format de fichier est pas BMP !\n");
        }
        close(fileR);
    } 
    return 0;
}