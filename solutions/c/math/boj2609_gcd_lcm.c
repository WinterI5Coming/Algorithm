#include <stdio.h>

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    int gcd = 0;
    int lcm = 0;

    int devide = N;
    if (N < M) {
        devide = M;
    }

    while (devide > 0) {
        if (N % devide == 0 && M % devide == 0) {
            gcd = devide;
            break;
        }

        devide--;
    }

    int multiply = 1;
    while ((N * multiply) % M != 0) {
        multiply++;
    }
    lcm = N * multiply;

    printf("%d\n%d", gcd, lcm);

    return 0;
}