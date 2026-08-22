"""
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
다음 소스와 같은 C++함수가 존재한다.
fibonacci(N)을 호출 할 때, 0과 1이 각각 몇 번씩 호출되는지 구한다
"""
"""
f(0) => 1: 0, 0: 1
f(1) => 1: 1, 0: 0
f(2) => f(1) + f(0) => 1: 1, 0: 1
f(3) => f(2) + f(1) => (f(1) + f(0)) + f(1) => 1: 2, 0: 1
f(4) => f(3) + f(2) => (f(2) + f(1)) + (f(1) + f(0)) 
                => ((f(1) + f(0)) + f(1)) + (f(1) + f(0)) => 1: 3, 0: 2
                
즉, 점화식은 다음과 같다 => a(n) = a(n-1) + a(n-2)
"""
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # dp = [[0, 0]] * (N + 2)
    # => 이런식으로 하게 되면 얕은 복사라서, 내부 리스트가 전부 같은 객체를 공유하게 되므로 위험할 수 있다.
    # 따라서 다음과 같이 변경
    dp = [[0, 0] for _ in range(N + 2)]
    dp[0], dp[1] = [1, 0], [0, 1]

    for i in range(2, N + 1):
        dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

    # print(dp)
    print(*dp[N])
