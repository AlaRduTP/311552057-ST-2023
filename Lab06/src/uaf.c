#include <stdio.h>
#include <stdlib.h>

int main() {
    char * s = (char *)malloc(sizeof(char));
    *s = '\0';
    free(s);
    puts(s);
}
