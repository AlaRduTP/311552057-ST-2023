#include <stdio.h>
#include <stdlib.h>

int main() {
    char * s = (char *)malloc(sizeof(char));
    s[1] = '\0';
    puts(s);
}
