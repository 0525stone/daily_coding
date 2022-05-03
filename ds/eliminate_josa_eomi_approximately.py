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


def eliminate_josa_eomi_approximately_regex(text):
    result = ''

    # read josa, eomi files
    eomi_filename = './data/JosaEomi/EOMI.TXT'
    josa_filename = './data/JosaEomi/JOSA.TXT'
    eomi = read_josa_eomi(eomi_filename)
    josa = read_josa_eomi(josa_filename)

    # 입력 text와 eomi, josa를 비교하여 없는 것들 제거
    for em in eomi:
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
        if em in text:
            print(f'it has {em}\nbefore {text}')
            # text = re.sub(r'{em}', '', text)   # em 다음에 스페이스(공백) 있는 것을 포함시켜야함(공백문자 표현식 있을 것임)
            # text = re.sub(r'[^가-힣]', '', text)
            text = re.sub(em, '', text)
            print(f'after {text}')


    result = '현수 술주정뱅이'

    return result


# TODO : 이름이 이게 맞는지.. 이 프로그램 안에서는 조사,어미만 읽어오는 것이니까 이렇게 하는게 맞을까?
def read_josa_eomi(filename='./data/JosaEomi/EOMI.TXT'):
    # JosaEomi/ EOMI.TXT  JOSA.TXT
    with open(filename,'r', encoding='euc-kr') as f:
        dumps = f.read()
        dump = dumps.split('\n')
        
        # if에 사용할 eomi 조건문으로 사용하기 위한 문자열
        eomi_if = ' | '.join(dump)
        # print(f'" {eomi_if} "')
    
    return dump[:-1]  # 마지막에 공백 문자가 있어서 그것은 제외시켜줘야함
        

def test_josa_eomi():
    # test : read_josa_eomi()  => 직접 일일이 셀 수 없으니까, txt 파일의 line 수로 확인
    eomis = read_josa_eomi('./data/JosaEomi/EOMI.TXT')
    assert len(eomis)==744
    josas = read_josa_eomi('./data/JosaEomi/JOSA.TXT')
    assert len(josas)==429
    print('read_josa_eomi test done')
    



    eliminate_josa_eomi_approximately_regex('이거하려면 이것들이 필요하련만 과연?')


    # test final result
    text = '현수는 술주정뱅이이다.'
    assert eliminate_josa_eomi_approximately_regex(text)=='현수 술주정뱅이'
    text = '알코올 의존증을 치료하려면 무엇이 필요할까?'
    assert eliminate_josa_eomi_approximately_regex(text)=='알코올 의존증 치료 필요'
    text = '자전거 여행을 가고 싶다.'
    assert eliminate_josa_eomi_approximately_regex(text)=='자전거 여행 가 싶'
    text = '거짓말로 들통 났다.'
    assert eliminate_josa_eomi_approximately_regex(text)=='거짓말 들통 났'

if __name__=="__main__":
    test_josa_eomi()