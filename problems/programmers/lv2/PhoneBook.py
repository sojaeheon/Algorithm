# Programmers 전화번호 목록
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 난이도: LV2

# 입력
# 전화번호를 담은 배열 phone_book

# 구해야할 것
# 어떤 번호가 다른 번호의 접두어인 경우 False, 그렇지 않으면 True

# 제한사항
# phone_book의 길이는 1이상 1,000,000 이하 -> 최소 O(N)
#   각 전화번호의 길이는 1이상 20이하
#   같은 전화번호가 중복해서 들어있지 않다.

def solution(phone_book):

    sort_phone_book = sorted(phone_book)

    for current_phone, next_phone in zip(sort_phone_book, sort_phone_book[1:]):
        if next_phone.startswith(current_phone):
            return False

    return True



if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))
