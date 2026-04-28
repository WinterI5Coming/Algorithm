#include <stdio.h>

int main(void)
{
    int ch, cm, cs;
    int sh, sm, ss;

    // scanf는 단순히 값만을 읽는 것이 아니라,
    // 입력 패턴 자체를 매칭한다.
    scanf("%d:%d:%d", &ch, &cm, &cs);
    scanf("%d:%d:%d", &sh, &sm, &ss);

    int current = cs + cm * 60 + ch * 60 * 60;
    int start = ss + sm * 60 + sh * 60 * 60;

    int remain = start - current;

    // 임무시 시작 시간(start)가 더 작아서 음수가 나온 경우 
    // => 24시간으로 더해서 역으로 만들어줘야 한다.
    // => Ex. 현재 시간 13시, 임무 시작 시간 8시 => 남은 시간은 19시 인데 8 - 13 = -5,
    //                                                => 따라서 -5 + 24 = 19
    if (remain <= 0) {
        remain += 24 * 60 * 60;
    }

    int rh = remain / 3600;
    remain -= rh * 3600;

    int rm = remain / 60;
    remain -= rm * 60;

    // %02d => 2칸으로 출력하되, 빈칸은 0으로 채워라.
    printf("%02d:%02d:%02d\n", rh, rm, remain);

    return 0;
}