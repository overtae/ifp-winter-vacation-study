# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 첫 줄에 합  
# 둘째 줄에 차,  
# 셋째 줄에 곱,  
# 넷째 줄에 몫,  
# 다섯째 줄에 나머지,  
# 여섯째 줄에 나눈 값을 순서대로 출력한다.  
# (실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)  
# 내 풀이)
a, b = map(int, input().split())
print( a+b )
print( a-b )
print( a*b )
print( a//b )
print( a%b )
print( round(a/b, 2) )
# 강의 풀이)
a, b = map(int, input().split())
print( a+b )
print( a-b )
print( a*b )
print( a//b )
print( a%b )
print( round(a/b, 2) )