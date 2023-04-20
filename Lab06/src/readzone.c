#include <stdio.h>

#define ARRSIZE 8
#define BYPASS ARRSIZE + 8

int main() {
    int a[ARRSIZE], b[ARRSIZE];
    a[BYPASS] = 87;
    printf("%d\n", b[0]);
}
