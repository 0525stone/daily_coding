#-*- coding: utf-8 -*-
"""
1. interface 규정 - eliminate_josa_eomi_approximately(context) = eliminated_context

"""
import re

def eliminate_josa_eomi_approximately_mecab():
    """
    나중에 해야할 것
    - 전체 프로세스에서 1번으로 이것을 거치고 unknown 으로 출력이 나오면 2번으로 넘어감
    """
    pass


# TODO : 이름이 이게 맞는지.. 이 프로그램 안에서는 조사,어미만 읽어오는 것이니까 이렇게 하는게 맞을까?
def read_josa_eomi(filename='./data/JosaEomi/JOSA.TXT'):
    # JosaEomi/ EOMI.TXT  JOSA.TXT
    with open(filename,'r', encoding='euc-kr') as f:
        word_dumps = f.read()
        word_dump = word_dumps.split('\n')
        
        # if에 사용할 eomi 조건문으로 사용하기 위한 문자열
        dump4if = ' |'.join(word_dump[:-1])
    
    return word_dump[:-1], dump4if  # 마지막에 공백 문자가 있어서 그것은 제외시켜줘야함


def eliminate_josa_eomi_approximately_regex_loop(text, sub1='', sub2=''):
    # for문으로 일일이 조사어미와 비교하여 제거
    # 입력 text와 eomi, josa를 비교하여 없는 것들 제거
    for sub in sub1:
        """
        for문으로 불용어를 제거할 경우, 하나씩 제거하는 것이 되어서, 단어가 점점 사라질 수 있지 않나???
        ex
        불용어 : 가, 로, 의, 다...

        문장 : 주의가 부족했다.

        예상 출력 : 주 부족했

        위와 같은 상황이 발생할 듯?
        따라서, or구문으로 전체를 잡아서 해줘야 깔끔하게 사라질 것으로 예상..
        또는 불용어 부분을 /와 같은 특수문자로 바꿔놓고 마지막에 특수문자를 제거하는 식으로 해도 될 듯
        """
        # 문장 부호 빈칸으로 바꿈
        text = re.sub(r".", " ", text) 
        # text = re.sub(r"([?.,!¿])", " ", text) 
        # text = re.sub(r'\n', ' ',text)

        if f'{sub} ' in text:
            print(f'it has {sub}\nbefore {text}')
            # text = re.sub(r'{em}', '', text)   # em 다음에 스페이스(공백) 있는 것을 포함시켜야함(공백문자 표현식 있을 것임)
            # text = re.sub(r'[^가-힣]', '', text)
            text = re.sub(f'{sub} ', ' ', text)
            print(f'after {text}')

    return text.strip()



def eliminate_josa_eomi_approximately_regex_ifor(text, subs1='', subs2=''):
    """
    subs1, subs2 는 불용어들을 '|'로 묶어논 문자열 

    선택 
    - subs1,2를 불용어를 포함한 리스트형으로 받아야할 지
    - subs1,2를 불용어를 포함한 | 연산자로 묶인 문자열로 받아야할 지
    """
    # preprocess for sentence
    text = re.sub(r"([?.,!¿])", " ", text) 
    # text = re.sub(r'"','',text)
    
    print(f'before\t{text}')
    
    if subs2:
        """
        subs1, subs2를 하나로 묶어서 큰 뭉태기 만들어야함
        """
        # combine subs1, subs2 to subs3
        subs1_raw = set(subs1.split(' |'))
        subs2_raw = set(subs2.split(' |'))
        subs3_raw = subs1_raw | subs2_raw
        subs3 = ' |'.join(subs3_raw)
        text = re.sub(subs3, ' ', text)

        print(f'after2\t{text}')
    else:
        text = re.sub(subs1, ' ', text)
        print(f'after1\t{text}')

    return text.strip()


# 사실상 main
def test_josa_eomi():

    # text1 = '이건 되야하는데.'
    # pat1 = '데'
    # assert re.sub(f'{pat1}','',text1)=='이건 되야하는.'

    # print('\n성공\n')
    # assert False



    # test : read_josa_eomi()  => 직접 일일이 셀 수 없으니까, txt 파일의 line 수로 확인
    eomis, eomis_if = read_josa_eomi('./data/JosaEomi/EOMI.TXT')
    assert len(eomis)==744
    josas, josas_if = read_josa_eomi('./data/JosaEomi/JOSA.TXT')
    assert len(josas)==429
    print('read_josa_eomi test done')



    # test : eliminating josa/eomi
    """
    1. test를 할 때, 처음에는 josas 만으로 잘 제거하는지 확인\
    2. eomis, josas 전부로 test 해볼 것
    3. context(문장들) 단위로 test 해볼 것
    * 문장부호는 지울 필요 없음 어미, 조사만 지우면 됨
    """
    texts = ['알코올 의존증을 치료할 생각이 있을쏘냐?', '자전거 여행을 가고 싶다.',  '거짓말로 들통 났다.', '현수는 술주정뱅이다.', '주의가 부족했다.']
    answers_josa = ['알코올 의존증 치료할 생각 있을쏘냐', '자전거 여행 가 싶', '거짓말 들통 났', '현수 술주정뱅' , '주의 부족했']  # 술주정뱅이=>술주정뱅
    answers_josa_eomi = ['알코올 의존증 치료할 생각 있', '자전거 여행 가 싶', '거짓말 들통 났', '현수 술주정뱅' , '주의 부족했']  # 술주정뱅이=>술주정뱅
    
    for text, answer in zip(texts, answers_josa):
        assert eliminate_josa_eomi_approximately_regex_ifor(text, josas_if)==answer
    print('only josa elimination test is done')

    for text, answer in zip(texts, answers_josa_eomi):
        assert eliminate_josa_eomi_approximately_regex_ifor(text, eomis_if, josas_if)==answer

    print('current test cases all done')

    long_context = ['분명 툭툭 던지는 말에 불과한데도, 그 속에 핵심이 있다.', 
    '인공지능은 동적 컴퓨팅 환경에 내장된 알고리즘을 생성하고, 적용하여 인간의 지능을 모방하는 기초 지능입니다.',
    '머스크는 이전에 AI가 궁극적으로 인간의 노동력을 대체할 것이고 미래의 AI가 지구에 사람이 필요하지 않다고 결정할 위험이 있다고 밝히기도 했다.머스크는 비즈니스인사이더라는 매체에 “AI의 진로에 대해 우려를 가질 필요가 있다”며 “AI에 대해 가장 틀린 사고를 하는 사람들이 내가 아는 가장 똑똑한 사람들로, 이는 컴퓨터가 그들보다 똑똑해지는 것을 예상하지 못하기 때문이다. 이는 논리적 오류이고 그들이 생각하는 것보다 더 어리석다는 것을 보여준다”고 하기도 했다.']
    long_answer =  []

    for context in long_context:
        print(eliminate_josa_eomi_approximately_regex_ifor(context, josas_if, eomis_if))






    # # eliminate_josa_eomi_approximately_regex_loop 는 폐기(for 문으로 돌리는 것은 말이 안됨)    
    # for text, answer in zip(texts, answers):
    #     assert eliminate_josa_eomi_approximately_regex_loop(text, josas)==answer

if __name__=="__main__":
    test_josa_eomi()
