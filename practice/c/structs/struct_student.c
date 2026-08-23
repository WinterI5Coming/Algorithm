//
// Created by Winter on 2026-07-28.
//

/*
 * 학생 구조체 선언 후 3명의 정보를 입력받아 평균 점수가 가장 높은 학생을 출력한다.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 학생 구조체
// typedef struct
// {
//     char name[30];
//     int score;
// } Student;

typedef struct
{
    char* name;
    int score;
} Student;

int main(void)
{
    Student stu_1;

    // 문자열 할당 방법
    // - 고정 크기 배열

    // 직접 복사
    strcpy(stu_1.name, "james");

    // 입력받을 때
    scanf("%29s", stu_1.name); // 버퍼 오버플로우 방지로 29자로 제한

    // fgets 사용 (공백 포함 가능)
    fgets(stu_1.name, sizeof(stu_1.name), stdin);
    stu_1.name[strcspn(stu_1.name, "\n")] = '\0'; // 개행 문자 제거

    stu_1.score = 90;

    // - 동적 할당 방식 => name을 포인터로 선언해야 한다

    // 1. 메모리 할당
    stu_1.name = malloc(30); // 도는 strlen(입력문자열) + 1
    if (stu_1.name == NULL)
    {
        // 에러 처리
    }
    // 2. 문자열 복사
    strcpy(stu_1.name, "steve");

    // 또는 한 번에 진행하는 것도 가능하다. (= 1+2)
    stu_1.name = strdup("steve"); // strdup은 malloc + strcpy를 한 번에 해준다.

    // 사용 후 반드시 해제
    free(stu_1.name);
    stu_1.name = NULL;

    /*
     * 그렇다면 여러 명을 동적 배열로 만들려면 어떻게 해야할까?
     *      1. 먼저 학생 배열을 만든다.
     *      2. 순회하면서 name과 score 입력
     *      3. 해제
     */
    int N;
    Student* students = malloc(sizeof(students) * N);

    for (int i = 0; i < N; i++)
    {
        students[i].name = malloc(30);
        scanf("%29s", students[i].name);
        scanf("%d\n", &students[i].score);
    }

    for (int i = 0; i < N; i++)
    {
        free(students[i].name);
    }
    free(students);


    return 0;
}
