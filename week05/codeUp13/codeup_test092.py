# 함께 문제 푸는 날

# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 
# 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 
# 풀게 되는 그날은 언제일까?

# 예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 
# 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 
# 함께 문제를 풀게 된다.

# 입력
# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 
# 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

a, b ,c = map(int, input().split())
i = 1
while not(i%a==0 and i%b==0 and i%c==0):
    i = i + 1
print(i)
