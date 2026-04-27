#include <stdio.h>

int main() {
    
    int T;
    scanf("%d", &T);

    for (int test_case = 0; test_case < T; test_case++) {

        int R;
        char S[21];

        scanf("%d %s", &R, S);

        char *p = S;

        while (*p != '\0') {

            for (int repeat = 0; repeat < R; repeat++) {
                printf("%c", *p);
            }

            p++;
        }       
    }
    
    
    return 0;
}