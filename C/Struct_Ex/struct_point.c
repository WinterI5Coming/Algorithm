//
// Created by Winter on 2026-07-28.
//
/*
 * 2차원 좌표 구조체 만들고, 두 점 사이 유클리드 거리 계산하는 함수 작성한다.
 */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    double x;
    double y;
} Point;


static double euclidean_dist(Point* point_a, Point* point_b)
{
    double dx = point_b->x - point_a->x;
    double dy = point_b->y - point_a->y;

    return sqrt(dx * dx + dy * dy);
}


int main(void)
{
    // 두 점을 입력 받는다고 가정한다.
    int N = 2;
    Point* points = malloc(sizeof(Point) * N);
    if (points == NULL)
    {
        printf("메모리 할당 실패\n");
        return 1;
    }

    for (int i = 0; i < N; i++)
    {
        scanf("%lf", &points[i].x);
        scanf("%lf", &points[i].y);
    }

    // double answer = euclidean_dist(points[0], points[1])
    double answer = euclidean_dist(&points[0], &points[1]);

    printf("answer is %.2f\n", answer);

    free(points);

    return 0;
}
