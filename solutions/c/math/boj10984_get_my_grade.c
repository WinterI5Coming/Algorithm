#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    for (int term = 0; term < T; term++) {

        int N;

        scanf("%d", &N);

        int total_c = 0;
        float total_g = 0.0;
        for (int i = 0; i < N; i++) {
            int c;
            float g;
            scanf("%d %f", &c, &g);

            total_c += c;
            total_g += c * g;
        }

        printf("%d %.1f\n", total_c, total_g / total_c);
    }

    return 0;
}