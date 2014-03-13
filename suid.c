#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
 
int main(void)
{
    printf("Real UID\t= %d\n", getuid());
    printf("Effective UID\t= %d\n", geteuid());
    printf("Real GID\t= %d\n", getgid());
    printf("Effective GID\t= %d\n", getegid());
 
    return EXIT_SUCCESS;
}
 
