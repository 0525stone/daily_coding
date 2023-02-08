"""
해시 문제
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        if phone2.startswith(phone1):
            answer = False
            return answer

    return answer

if __name__=="__main__":
    print("phonebook")
    
    phone_book = ["119", "97674223", "1195524421"]
    answer = solution(phone_book)
    assert answer==False
    print('corret')

    phone_book = ["123","456","789"]
    answer = solution(phone_book)
    assert answer==True
    print('corret')

    phone_book = ["12","123","1235","567","88"]
    answer = solution(phone_book)
    assert answer==False
    print('corret')

    print('all done')