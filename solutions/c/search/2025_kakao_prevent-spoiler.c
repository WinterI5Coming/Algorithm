/*
 * 카카오톡에는 스포방지 기능을 제공한다.
 * => 해당 기능을 활용하여 하나의 메시지 곳곳에 기능을 적용해서 나한테 메시지
 * 전송했다.
 * => 메시지 시작부터 왼쪽->오른쪽 순서로 스포방지 구간 하나씩 클릭을 하게 되고
 *      => 그렇게 공개되는 단어들 중, 중요한 단어가 몇 개인지 확인하는 것이
 * 목적이다.
 *
 * 단어 규칙
 *      - 단어는 공백으로 구분되고, 알파벳(소문자) + 숫자로만 구성되었다.
 *      - 단어 문자열의 인덱스 중 하나 이상이 스포방지 구간에 포함되는 경우,
 *          해당 단어는 스포방지 단어로 간주한다.
 *      - 한 단어가 여러 개의 스포방지 구간에 걸쳐 있을 수 있고,
 *          하나의 스포방지 구간에 여러 단어가 포함될 수도 있다.
 *      - 스포방지 구간 클릭해 모든 문자 공개되었을 때, 아래의 모든 조건
 * 만족해야 중요한 단어이다.
 *          1. 스포방지 단어이어야 한다.
 *          2. 메시지의 스포방지 구간이 아닌 구간에 등장한 적 없어야 한다.
 *          3. 이전에 공개된 스포방지 단어와 중복 불가이다.
 *          4. 여러 단어가 동시에 공개된 경우, 왼쪽부터 하나씩 중요 단어인지
 * 판단한다.
 *
 *  문자열(message)와 스포방지가 적용된 구간을 나타내는 2차원 정수 배열이 주어질
 * 때, 스포방지 단어 중 중요한 단어의 수를 반환한다.
 */

/*
 * 1. 주어진 스포방지 구간을 순회하면서 단어를 수집한다.
 * 2. 수집된 단어들을 대상으로 다시 전체 문자열을 대상으로 순회하면서 중요
 * 단어인지 검사한다.
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_word_start(const char* message, int position)
{
    while (position > 0 && message[position - 1] != ' ')
    {
        position--;
    }

    return position;
}

int find_word_end(const char* message, int position)
{
    int message_len = (int)strlen(message);

    while (position + 1 < message_len && message[position + 1] != ' ')
    {
        position++;
    }

    return position;
}


char* copy_word(const char* message, int word_start, int word_end)
{
    int word_len = word_end - word_start + 1;

    char* word = malloc(sizeof(char) * (word_len + 1));

    for (int i = 0; i < word_len; i++)
    {
        word[i] = message[word_start + i];
    }

    word[word_len] = '\0';

    return word;
}


// spoiler_ranges_rows는 2차원 배열 spoiler_ranges의 행 길이,
// spoiler_ranges_cols는 2차원 배열 spoiler_ranges의 열 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을
// 복사해서 사용하세요.
int solution(const char* message, int** spoiler_ranges,
             size_t spoiler_ranges_rows, size_t spoiler_ranges_cols)
{
    int answer = 0;

    // 스포 구간에서 발견한 단어 저장한다.
    char** spoiler_words = malloc(sizeof(char*) * spoiler_ranges_rows);

    for (size_t i = 0; i < spoiler_ranges_rows; i++)
    {
        int range_start = spoiler_ranges[i][0];
        int range_end = spoiler_ranges[i][1];

        // 스포구간의 시작 문자가 속한 단어의 시작 위치
        int word_start = find_word_start(message, range_start);
        // 스포구간의 마지막 문자가 속한 단어의 끝 위치
        int word_end = find_word_end(message, range_end);

        spoiler_words[i] = copy_word(message, word_start, word_end);

        // 수집된 단어 확인
        printf("%zu번 스포 구간: %s\n", i, spoiler_words[i]);
    }

    for (size_t i = 0; i < spoiler_ranges_rows; i++)
    {
        free(spoiler_words[i]);
    }

    free(spoiler_words);

    return answer;
}
