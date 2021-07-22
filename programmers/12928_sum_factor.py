"""
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.

"""

def solution1(n):
    sum = 0
    for i in range(1,n+1):
        if n%i == 0:
            sum = sum+i
    return sum

# programmers solution
def solution2(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

n = 12	# 28
n = 5	# 6
ans = solution1(n)
print(ans)

