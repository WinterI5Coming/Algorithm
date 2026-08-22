#include <stdio.h>
#include <string.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    for (int tc = 0; tc < T; tc++) {

        int p;
        scanf("%d", &p);

        char expensive_player_name[21] = "";
        int expensive_player_price = 0;

        for (int i = 0; i < p; i++) {
            int player_price = 0;
            char player_name[21];

            scanf("%d %s", &player_price, player_name);

            if (expensive_player_price < player_price) {
                // C에서는 문자열이 사실상 배열이기 때문에, 배열끼리의 대입은 불가하다.
                // 따라서 문자열 복사를 해야 한다. => 가장 일반적인 방법이 바로 strcpy() 사용.
                strcpy(expensive_player_name, player_name);
                expensive_player_price = player_price;
            }
        }

        printf("%s\n", expensive_player_name);
    }
    
    return 0;
}