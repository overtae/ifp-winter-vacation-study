# n개의 정수가 순서대로 입력된다.
# (단 n의 최대 개수는 알 수 없다.)

# n개의 입력된 정수를 순서대로 출력해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.

# 입력
# 첫 줄에 정수의 개수 n이 입력되고,
# 두 번째 줄에 n개의 정수가 공백을 두고 입력된다.
# 출력
# n개의 정수를 한 개씩 줄을 바꿔 출력한다
n = int(input())
number = list(map(int, input().split()))

# 1
def goto(number, n, i):
    if i == n:
        return
    print(number[i])
    i += 1
    goto(number, n, i)
goto(number, n, 0)

# 2 reverse 사용
number.reverse()
def goto(number, n):
    print(number[n])
    n -= 1
    if n == -1:
        return
    goto(number, n)
goto(number, n-1)