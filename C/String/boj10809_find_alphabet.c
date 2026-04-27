#include <stdio.h>

int main() {

    char S[101];
    int pos[26];

    scanf("%s", S);

    for (int i = 0; i < 26; i++) {
        pos[i] = -1;
    }

    for (int i = 0; S[i] != '\0'; i++) {
        // C에서 문자열을 서로 뺀 후 int로 변환하면 정수로 바뀌는 것을 이용한다.
        int idx = S[i] - 'a';

        if (pos[idx] == -1) {
            pos[idx] = i;
        }
    }

    // 출력
    for (int i = 0; i < 26; i++) {
        printf("%d ", pos[i]);
    }    

    
    return 0;
}