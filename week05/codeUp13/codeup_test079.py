# 원하는 문자가 입력될 때까지 반복 출력하기

# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# 입력
# 문자들이 1개씩 계속해서 입력된다.

# 출력
# 'q'가 입력될 때까지 입력된 문자를 줄을 바꿔 한 줄씩 출력한다.

listChar = list(input().split())

# 1
for i in listChar:
    print(i)
    if i == 'q':
        break
# 2
i = 0
while listChar[i] != 'q':
    print(listChar[i])
    i += 1
print(listChar[i])
