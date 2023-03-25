"""
1. 우상향 문제
숫자 몇개를 지웠을 때 우상향 배열이 되는가
0~2 까지는 그냥 출력
3이상은 -1로 출력
# input
45 62 15 23 77 105
# result
2

"""



# 문제마다 주어지는 형태 복사 붙여넣기하기
def solution(text):
    # bfs, dfs 
    # text를 지워주기

    # 우상향인지 확인해보기
    list1 = [0 if i2>i1 else 1 for i1, i2 in zip(text, text[1:])]
    print(list1)



    return 0



if __name__=="__main__":
    text = "45 62 15 23 77 105"
    l = [int(t) for t in text.split()]
    print(l)
    
    # test case 추가해서 답 확인해주기
    text1 = "45 62 15 23 77 105"
    answer=solution(text1)
    assert answer==0, answer

    print("all done")

