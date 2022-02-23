import sys
input = sys.stdin.readline

def palindrome(s, left, right):

    while left < right:  # 중간까지만 검사하면 됨
        # i와 j 위치에 둘 다 알파벳 문자가 있으면 두 문자를 비교하고 다르면 회문이 아님
        if s[left].lower() != s[right].lower():
            return False
        # i와 j 위치에 두 문자를 비교하고 같으면 다음 비교 대상으로 넘어감
        else:
            left += 1
            right -= 1
    return True


def ispalindrome(s, left, right):
    if s == s[::-1]:
        return 0
    else:
        while left < right:
            if s[left] != s[right]:
                # left에서 한 칸 건너 뛰기
                check_left = palindrome(s, left + 1, right)
                # right에서 한 칸 건너 뛰기
                check_right = palindrome(s, left, right - 1)

                # 회문이면
                if check_left or check_right:
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1


n = int(input())

for _ in range(n):
    str = input().rstrip()
    left = 0  # 문자열의 앞에서 비교할 위치
    right = len(str) - 1  # 문자열의 뒤에서 비교할 위치

    # 회문
    if palindrome(str, left, right) == True:
        print(0)
    # 유사회문
    elif ispalindrome(str, left, right) == True:
        print(1)
    else:
        print(2)
