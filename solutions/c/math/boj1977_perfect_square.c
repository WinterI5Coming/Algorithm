#include <stdio.h>

int main(void)
{
    int M, N;
    scanf("%d %d", &M, &N);

    int square_sum = 0;
    int min_square = -1;

    for (int i = M; i < N + 1; i++) {
        // 완전제곱수를 어떻게 판단하는가?
        for (int j = 1; j * j < N + 1; j++) {
            int square = j * j;

            if (i == square) {
                square_sum += i;

                if (min_square == -1) {
                    min_square = i;
                }
                break;
            }
        }
    }

    if (min_square == -1) {
        printf("%d\n", -1);
    }
    else {
        printf("%d\n%d", square_sum, min_square);
    }
    
    return 0;
}