#include <stdio.h>

int main() {

    char S[1000001];
    fgets(S,sizeof(S), stdin);

    int word_cnt = 0;
    int in_word = 0;

    char *p = S;

    while (*p != '\0') {

        if (*p != ' ' && *p != '\n') {
            // 빈 공백이 아닌 경우 ==> word_cnt +=1
            if (!in_word) {
                word_cnt += 1;
                in_word = 1;
            }
        } else {
            // 빈 공백인 경우
            in_word = 0;
        }
        
        p++;        
    }

    printf("%d", word_cnt);
    
    return 0;
}